from django.urls import path
from account.views import register_user, Login_users

urlpatterns = [
    path("login/", Login_users.login_user, name="login"),
    path("logout/", Login_users.logout_user, name="logout"),
    path("register/", register_user.register, name="register")
]