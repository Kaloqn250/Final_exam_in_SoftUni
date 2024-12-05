from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from exam_project1_1.accounts.forms import CustomUserCreationForm


class CreateProfileView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class ProfileDetailView(DetailView):
    model = get_user_model()
    template_name = 'registration/profile_details.html'
