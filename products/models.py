from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)
    comments = models.TextField(max_length=1000)

class User(models.Model):
    pass
