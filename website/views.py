from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, permission_required

from .forms import Registerform, Postform
from .models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'main/home.html')

@login_required(login_url="/login")
def post(request):
    form = Postform() # Initialize form at the beginning
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            print(post.author)
            post.save()
            return redirect('/home')
    return render(request, 'main/post.html', {'form': form})


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
    else:
        form = Registerform()

    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/home')