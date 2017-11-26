from django.db import models

# Create your models here.
#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime


# Create your models here.
    




#
class Country(models.Model):
    name = models.CharField(max_length=500)
    dicts = models.TextField(max_length=500000)
    date = models.CharField(max_length=500)
    