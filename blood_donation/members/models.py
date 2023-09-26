from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(null=True,max_length=255)
    age = models.IntegerField(null=True)
    password = models.CharField(null=True,max_length=255)
    phone = models.IntegerField(null=True)
    address =  models.CharField(null=True,max_length=255)