from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Users

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())
def register(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render())

def allUsers(request):
  databaseUsers  = Users.objects.all().values()
  template = loader.get_template("all_members.html")
  context = {
    "users":databaseUsers,
  }
  return HttpResponse(template.render(context,request))