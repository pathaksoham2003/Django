from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(null=True,max_length=25)
    age = models.IntegerField(null=True)
    email = models.CharField(null=True, max_length=50)
    password = models.CharField(null=True,max_length=25)
    phone = models.IntegerField(null=True)

class Bloods(models.Model):
    byid = models.IntegerField(null=True)
    byuser = models.CharField(null=True,max_length=25)
    litresofblood = models.IntegerField(null=True)
    bloodGroup = models.CharField(null=True,max_length=10)
