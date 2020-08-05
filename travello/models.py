from django.db import models

# Create your models here.

class destinations(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default="False")
