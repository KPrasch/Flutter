from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from accounts.models import Member


class Flutt(models.Model):
    author = models.ForeignKey(Member)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        result = "{} {}".format( self.author, self.created)
        return result

    def __repr__(self):
        result = "{} {}".format( self.author, self.created)
        return result
