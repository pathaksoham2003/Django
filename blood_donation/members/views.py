from django.shortcuts import render
from .models import Users

def index(request):
  return render(request,"index.html")

def login(request):
    return render(request, 'login.html')

def register(request):
  return render(request,"register.html")

def all_users(request):
  databaseUsers  = Users.objects.all().values()
  context = {
    "users":databaseUsers,
  }
  return render(request,"all_users.html",context)

def details(request , id):
  user = Users.objects.get(id=id)
  context = {
    "user" : user
  }
  return render(request,"details.html",context)

def profile(request):
  if(request.POST):
    name = request.POST["name"]
    age = request.POST["age"]
    email = request.POST["email"]
    password = request.POST["password"]
    phone = request.POST["phone"]
    
    context = {
      "name":name,
      "age":age,
      "email":email,
      "password":password,
      "phone":phone,
    }
    dbname = Users(name=name,age=age,email=email,password=password,phone=phone)
    dbname.save()
    print(dbname)
    return render(request,"profile.html",context)
  else:
    print(name,email,password)
    return render(request,"login.html")
    