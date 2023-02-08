from django.urls import path
from home import views
urlpatterns = [
    path("create_ticket/", views.create_ticket),
    path("create_review/", views.create_review),
    path("home_page/", views.home_page),
    path("subscription_page/", views.subscription_page)
]