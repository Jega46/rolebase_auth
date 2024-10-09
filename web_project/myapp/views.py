# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pyexpat.errors import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import CustomUser

def get_user_role(user):
    if user.is_superuser:
        return 'admin'
    elif user.groups.filter(name='Editors').exists():
        return 'editor'
    elif hasattr(user, 'user_role'):
        return user.user_role  # Fetch from a field if using a custom user model
    else:
        return 'viewer'




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_role = form.cleaned_data.get('user_role')  # Set user_role
            user.save()  
            auth_login(request, user)  # Use Django's built-in login function
            return redirect('home') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

       
        # Authenticate the user with the username and password
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
             if request.user.is_authenticated:
                user_role = request.user.user_role  # Retrieve the user_role directly from the user object.
                print(user_role) 
            
                return redirect('home') # Redirect to the 'home' page after successful login
        else:
            messages.error(request, "Invalid username or password.")  # Display error message
    
    return render(request, 'login.html')

# views.py



from django.shortcuts import render, redirect
from .models import Paragraph

from django.shortcuts import render, redirect, get_object_or_404
from .models import Paragraph
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    paragraph = Paragraph.objects.first()  # Get the first paragraph
    if request.user.is_authenticated:
        username = request.user.username
      
    # Check if the user is authenticated and get their role
    if request.user.is_authenticated:
        user_role = request.user.user_role  # Retrieve the user_role directly from the user object

    if paragraph is None:
        # Handle the case where there are no paragraphs
        return render(request, 'home.html', {'error': "No paragraphs available."})

    context = {
        'paragraph': paragraph,
        'username':username,
        'user_role': user_role,
        'show_create_button': paragraph is None,
        'is_admin': request.user.is_superuser,  # Check if the user is an admin
        'is_editor': request.user.groups.filter(name='Editors').exists(),  # Check if the user is in the Editors group
    }

    return render(request, 'home.html', context)
    
  #  return render(request, 'home.html', {
  #      'paragraph': paragraph,  # This could be None if no paragraph exists
  #      'can_edit': can_edit,  # Pass edit permission to the template
   #     'can_delete': can_delete,  # Pass delete permission to the template
   #     'user_role': user_role,  # Pass the user role to the template
   # })


def update_paragraph(request, id):
    paragraph = get_object_or_404(Paragraph, id=id)

    if request.method == 'POST':
        paragraph.content = request.POST['content']
        paragraph.save()
        return redirect('home')  # Redirect to home after updating

    return redirect('home')

def delete_paragraph(request, pk):
    # Fetch the paragraph object to delete
    paragraph = get_object_or_404(Paragraph, pk=pk)
    user_role = request.user.user_role  # Assuming you're using a custom user model

    # Ensure only admin can delete
    if user_role == 'admin':
        paragraph.delete()
        return redirect('home')  # Redirect after deletion

    # If the user doesn't have permission, redirect to home (or show an error)
    return redirect('home')

def create_paragraph(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        if content:
            Paragraph.objects.create(content=content)
        return redirect('home')  # Redirect to the home page after creation

    return redirect('home')