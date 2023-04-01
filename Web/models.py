from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

    def __unicode__(self):
        return f"{self.user}-token"


class Expense(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return f"Expense{self.date}-{self.amount}"


class Incom(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return f"Icome{self.date}-{self.amount}"
