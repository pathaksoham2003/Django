from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login , name ="members"),
    path('register/',views.register , name="register")
]
