from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    location = models.CharField(max_length=100)

    date = models.DateField(null=True, blank=True)

    capacity = models.IntegerField()