from django.urls import path
from home import views
urlpatterns = [
    #path("home/create_review/", views.create_review),
    #path("home/subscription_page/", views.subscription_page)
    path("home/", views.home_page),
    path("home/create_ticket/", views.create_ticket, name="ticket")
]