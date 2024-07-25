from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, permission_required


def login(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=user, password=password)
        if user is not None:
            return redirect('/')
        else:
            return render(request, 'Auth/login.html', {"message":"Invalid credentials"})
    return render(request, 'Auth/login.html')

def register(request):
    if request.method =="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if User.objects.filter(username=username).exists():
            return render(request, 'Auth/register.html', {"message":"Username already taken"})
        elif User.objects.filter(email=email).exists():
            return render(request, 'Auth/register.html', {"message":"Email associated with another account"})
        else:
            data = User.objects.create_user(username=username, email=email, password=password)
            if data is not None:
                return redirect("/")
    return render(request, 'Auth/register.html')

def logout_view(request):
    logout(request)
    return redirect('/home')