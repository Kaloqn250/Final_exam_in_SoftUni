from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from exam_project1_1.accounts.forms import CustomUserCreationForm, EditProfileForm
from exam_project1_1.accounts.models import Profile

UserModel = get_user_model()


class CreateProfileView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class ProfileDetailView(DetailView):
    model = UserModel
    template_name = 'registration/profile_details.html'

    # def get_success_url(self):
    #     return reverse_lazy('details', kwargs={'pk': self.request.user.pk})


class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.request.user.pk})


def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')