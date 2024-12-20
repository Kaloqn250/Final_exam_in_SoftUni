from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from exam_project1_1.accounts.models import Profile

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']




