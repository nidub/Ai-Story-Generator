from django.db import models
import datetime
from django.utils.timezone import now
# Create your models here.


class entries(models.Model):
    entry=models.CharField(max_length=1000)
    date=models.DateTimeField(default=now)

    def __str__(self):
        return self.entry


class stories(models.Model):
    story=models.CharField(max_length=1000)
    date=models.DateTimeField(default=now)

    def __str__(self):
        return self.entry


class generated(models.Model):
    generated_text=models.CharField(max_length=1000)
    date=models.DateTimeField(default=now)

    def __str__(self):
        return self.generated_text