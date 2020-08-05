from django.urls import path
from . import views

#create mapping for urls

urlpatterns = [
    path('', views.index, name="index"),    
]
