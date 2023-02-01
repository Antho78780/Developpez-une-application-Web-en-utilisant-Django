from django.urls import path
from account.views import Login_users, Register_users

urlpatterns = [
    path("login/",Login_users.print_login_html, name='login'),
    path("register/",Register_users.print_register_html, name='register')
]