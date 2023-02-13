from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from account.views import register_user

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html", next_page="login"), name="logout"),
    path("register/", register_user.register, name="register")
]