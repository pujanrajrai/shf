from datetime import datetime

from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    send_date = models.DateTimeField(auto_now_add=True)
    message_viewed = models.BooleanField(default=False)
