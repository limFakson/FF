from django.urls import path, include

from . import views, auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/login', auth_view.login, name='home'),
    path('auth/register', auth_view.register, name='sign-up'),
    path('auth/logout', auth_view.logout_view, name='logout'),
    path('post', views.post, name='post'),
]

