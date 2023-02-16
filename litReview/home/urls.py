from django.urls import path
from home import views
urlpatterns = [
    #path("home/create_review/", views.create_review, name="review"),
    #path("home/subscription_page/", views.subscription_page name="subscription")
    path("home/", views.home_page, name="home"),
    path("home/create_ticket/", views.create_ticket, name="ticket"),
]
