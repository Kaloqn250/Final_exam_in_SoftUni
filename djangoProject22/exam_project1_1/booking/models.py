from django.contrib.auth import get_user_model
from django.db import models

from exam_project1_1.events.models import Event


UserModel = get_user_model()


# Create your models here.
class Booking(models.Model):

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')
