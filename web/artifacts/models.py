import datetime
import os

from django.db import models
from django.utils import timezone


class Artifact(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.name


class Picture(models.Model):
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE)
    filename = models.CharField(max_length=100)
    image = models.ImageField()


