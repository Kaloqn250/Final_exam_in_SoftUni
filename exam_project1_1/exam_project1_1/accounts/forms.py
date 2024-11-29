from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from exam_project1_1.accounts.models import User


#
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
#
#
# class CreateProfileForm(ProfileForm):
#     pass

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)
