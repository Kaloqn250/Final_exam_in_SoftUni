from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from exam_project1_1.accounts.forms import CustomUserCreationForm, EditProfileForm
from exam_project1_1.accounts.models import Profile
from exam_project1_1.booking.models import Booking

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        bookings = Booking.objects.filter(user_id=self.kwargs['pk'])
        context['bookings'] = bookings
        return context

    # def get_success_url(self):
    #     return reverse_lazy('details', kwargs={'pk': self.request.user.pk})


class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'

    def get_object(self, queryset=None):
        # Get the profile of the logged-in user
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.request.user.pk})


class DeleteProfileView(DeleteView):
    pass


def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')