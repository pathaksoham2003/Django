from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login , name ="login"),
    path('register/',views.register , name="register"),
    path('allusers/', views.all_users , name = "allUsers"),
    path("allusers/details/<int:id>",views.details , name = "details")

]
