from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=40,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=40,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        blank=True,
        null=True,
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
