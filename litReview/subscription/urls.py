from django.urls import path
from subscription import views

urlpatterns = [
    path("home/subscription/", views.subscription, name="subscription")
]