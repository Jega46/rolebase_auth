from django.contrib import admin
from myapp.models import Paragraph
# Register your models here.
admin.site.register(Paragraph)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'user_role', 'is_staff', 'is_active']

admin.site.register(CustomUser, CustomUserAdmin)

