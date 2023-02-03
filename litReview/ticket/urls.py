from django.urls import path
from ticket import views
urlpatterns = [
    path("ticket/", views.ticket)
]