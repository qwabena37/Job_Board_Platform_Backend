from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (('admin', 'Admin'), ('user', 'User'))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def is_admin(self):
        return self.role == "admin" or self.is_staff


class UserProfile(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
