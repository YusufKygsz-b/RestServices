from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = None
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True,  default='default_username')

    USERNAME_FIELD = 'username'
    REQUIRE_FIELD = ['email']

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = "Kullanıcı"