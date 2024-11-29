from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from exam_project1_1.accounts.forms import RegisterForm


class CreateProfileView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class ProfileDetailView(DetailView):
    model = get_user_model()
    template_name = 'registration/profile_details.html'
