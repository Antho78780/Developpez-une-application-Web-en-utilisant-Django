from django.urls import path
from subscription import views

urlpatterns = [
    path("flux/subscription/", views.subscription, name="subscription")
]