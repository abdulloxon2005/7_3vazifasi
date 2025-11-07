from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CostomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True,blank=True)
    