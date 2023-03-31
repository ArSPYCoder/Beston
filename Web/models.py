from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Expense(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)




class Incom(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
