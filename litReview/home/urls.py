from django.urls import path
from home.views import TicketView, HomeView
urlpatterns = [
    path("home/", HomeView.home_page, name="home"),
    path("home/create_ticket/", TicketView.create_ticket, name="ticket"),
    #path("home/create_review/", views.create_review, name="review")
]
