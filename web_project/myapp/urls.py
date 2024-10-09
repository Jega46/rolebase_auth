from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.register, name='register'),
    path('home/', views.home, name='home'),


]