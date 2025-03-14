from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=300,unique = True)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    image = models.ImageField(max_length=300)
    