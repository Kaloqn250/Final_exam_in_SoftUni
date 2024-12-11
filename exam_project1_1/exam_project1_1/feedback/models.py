from django.contrib.auth import get_user_model
from django.db import models
from exam_project1_1.events.models import Event

User = get_user_model()


# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )

    comment = models.TextField()

    something = models.TextField()

    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)]

    )
    created_at = models.DateTimeField(auto_now_add=True)

