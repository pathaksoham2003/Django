from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(null=True,max_length=25)
    age = models.IntegerField(null=True)
    email = models.CharField(null=True, max_length=50)
    password = models.CharField(null=True,max_length=25)
    phone = models.IntegerField(null=True)