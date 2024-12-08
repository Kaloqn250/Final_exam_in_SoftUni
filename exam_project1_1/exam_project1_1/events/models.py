from django.db import models

from exam_project1_1.category.models import Category


class Event(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    location = models.CharField(max_length=100)

    date = models.DateField(null=True, blank=True)

    capacity = models.IntegerField()

    image = models.ImageField(upload_to='events_pictures')

    categories = models.ManyToManyField(
        Category,
        related_name='events'
    )

    def __str__(self):
        return self.name
