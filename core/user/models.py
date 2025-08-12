from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(("email address"), unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []