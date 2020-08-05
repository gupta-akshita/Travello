from django.urls import path
from . import views

#create mapping for urls

urlpatterns = [
    path('register', views.register, name="register"), 
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]
