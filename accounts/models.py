from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,primary_key=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # username is still required

    def __str__(self):
        return self.email