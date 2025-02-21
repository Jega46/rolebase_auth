    # -*- coding: utf-8 -*-
from __future__ import unicode_literals



# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User 

class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('viewer', 'Viewer'),
        ('editor','Editor')
    )
    user_role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES)
# models.py


class Paragraph(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content[:50]
    

 
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=50)  # Field to store the user's role
    # You can add more fields as needed
    bio = models.TextField(blank=True, null=True)  # Optional biography field
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


