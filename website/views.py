from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required

from .forms import Registerform
# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/home')
    
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('/login')
    else:
        form = Registerform()

    return render(request, 'registration/register.html', {'form': form})