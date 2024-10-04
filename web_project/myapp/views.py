# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# views.py

from django.shortcuts import render, redirect
from myapp.models import Paragraph 

def home(request):
    # Get the first content object (assuming only one paragraph exists)
    paragraph = Paragraph.objects.first()

    # Example user role logic (replace with actual logic from request.user)
    user_role = 'viewer'  # Example roles: 'admin', 'editor', or 'viewer'

    # Determine permissions based on user role
    can_edit = user_role in ['admin', 'editor']
    can_delete = user_role == 'admin'

    if request.method == 'POST':
        if 'edit' in request.POST and can_edit:  # Handling the edit action
            new_content = request.POST.get('content')
            paragraph.content = new_content
            paragraph.save()  # Save the updated content to the database
            return redirect('home')  # Redirect to avoid resubmission issues on refresh
        elif 'delete' in request.POST and can_delete:  # Handling the delete action
            paragraph.delete()  # Delete the paragraph
            return redirect('home')

    return render(request, 'home.html', {
        'paragraph': paragraph,
        'can_edit': can_edit,  # Pass edit permission to the template
        'can_delete': can_delete,  # Pass delete permission to the template
        'user_role': user_role,  # Pass the role to the template
    })

