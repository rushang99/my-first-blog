from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils import timezone


class Data_set(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    #user = models.ForeignKey(User)

    def publish(self):
        return self.created_date

class User_input(models.Model):
	from_date=models.DateTimeField(default=timezone.now)
	to_date=models.DateTimeField(default=timezone.now)
