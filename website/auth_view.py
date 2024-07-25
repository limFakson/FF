from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, permission_required


def login(request):
    return render(request, 'Auth/login.html')

def register(request):
    return render(request, 'Auth/register.html')

def logout_view(request):
    logout(request)
    return redirect('/home')