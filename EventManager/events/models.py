from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)