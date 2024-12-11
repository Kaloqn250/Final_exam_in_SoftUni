from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from exam_project1_1.accounts.managers import AppUserManager


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()





