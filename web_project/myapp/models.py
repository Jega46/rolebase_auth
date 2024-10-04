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
        ('editor','editor')
    )
    user_role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='viewer')
# models.py


class Paragraph(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50]
