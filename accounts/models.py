from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
# class Profile(models.Model): # Profile model
#     ROLE_CHOICES = (
#         ('admin', 'Admin'),
#         ('user', 'User'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE) # OneToOneField to User model
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"