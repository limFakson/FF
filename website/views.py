from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group, User

from .forms import Registerform
# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def register(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = Registerform()

    return render(request, 'forms/register.html', {'form': form})