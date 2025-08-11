from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    REQUIRED_FIELDS = ["age", "email"]
