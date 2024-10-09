# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Paragraph

class CustomUserCreationForm(UserCreationForm):
    user_role = forms.CharField(max_length=50, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_role']


