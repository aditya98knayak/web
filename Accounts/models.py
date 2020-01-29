from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone

# Create your models here.


class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    birthdate = models.DateField(default=django.utils.timezone.now)
    address = models.TextField(null=True, max_length=50)
    Gender = models.CharField(max_length=10, null=False, default="MALE")
    profile = models.ImageField(default="default.png",blank=True, null=True)



