from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    offline_name = models.CharField(max_length=999, blank=True, null=True)
    phone_number = models.CharField(max_length=14, help_text="A phone number including + and the country code")
    bio = models.TextField(null=True, blank=True)
    dob = models.DateTimeField(auto_now=False)
    last_active = models.DateTimeField(auto_now=True)
    likes_pickles = models.BooleanField(default=True)
    favors_llamas = models.NullBooleanField()

    def __str__(self):
        return self.phone_number
