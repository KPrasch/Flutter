from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Member


class Flutt(models.Model):
    URGENCY = (
        ('TOP', 'High Priority'),
        ('MEH', 'Do it later')
    )

    author = models.ForeignKey(Member, related_name='flutts')
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=3, choices=URGENCY)

    def get_exerpt(self, amount):
        result = self.body[0:amount]
        return result

    def __str__(self):
        result = "{} {}".format(self.author, self.created)
        return result

    def __repr__(self):
        result = "{} {}".format(self.author, self.created)
        return result
