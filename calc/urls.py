from django.urls import path
from . import views

#create mapping for urls

urlpatterns = [
    path('', views.home, name="home"), 
    path("add", views.add, name="add" )
]
