from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    infos = models.CharField(max_length=1000, default='')
    address = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=20, default='')