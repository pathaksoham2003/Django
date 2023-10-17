from django.shortcuts import render
from .models import Users

def index(request):
  return render(request,"index.html")

def login(request):
    return render(request, 'login.html',{"message":""})

def register(request):
  return render(request,"register.html",{"message":""})

def registeruser(request):
    if request.method == 'POST':
        name = request.POST["name"]
        age = request.POST["age"]
        email = request.POST["email"]
        password = request.POST["password"]
        phone = request.POST["phone"]

        # Check if the email already exists
        if Users.objects.filter(email=email).exists():
            return render(request, "register.html",{"message":"Email Already Exist"})
        
        context = {
            "name": name,
            "age": age,
            "email": email,
            "password": password,
            "phone": phone,
        }
        dbname = Users(name=name, age=age, email=email, password=password, phone=phone)
        dbname.save()
        return render(request, "profile.html", context)
    else:
        return render(request, "register.html",{"message":"Internal Error"})

def checkuser(request):
   if request.method =="POST":
      email = request.POST["email"]
      password = request.POST["password"]
      if Users.objects.filter(email=email).filter(password=password).exists():
         context = Users.objects.filter(email=email).values()
         return render(request,"profile.html",context)
      return render(request,"login.html",{"message":"Wrong Credentials"})
      
   

    

















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

def checkLogin(request):
   if request.method == 'POST':
      name = request.POST["name"]
      email = request.POST["email"]
      password = request.POST['password']
      db = Users.objects.filter(email=email).values()
      if db.password == password:
         return render(request,"profile.html",{"name":name,"email":email,"password":password})
      return render(request,"login.html")

