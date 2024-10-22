from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url="/login")
def post(request):
    
    return render(request, 'main/post.html')

