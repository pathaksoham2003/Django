from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('login/', views.login , name ="login"),
    path("checkuser",views.checkuser, name="profile"),
    path('register/',views.register , name="register"),
    path("registeruser",views.registeruser, name="profile"),
]