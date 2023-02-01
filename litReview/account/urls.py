from django.urls import path
from account import views as views_auth

urlpatterns = [
    path("login/", views_auth.login, name='login'),
    path("register/", views_auth.register, name='register')
]