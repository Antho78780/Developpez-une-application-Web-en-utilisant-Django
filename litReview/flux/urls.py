from django.urls import path
from flux import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "flux"

urlpatterns = [
    path("flux/", views.flux, name="flux"),
    path("flux/ticket/", views.create_ticket, name="ticket"),
    path("flux/posts/update_ticket/<ticket_id>", views.create_ticket, name="update-ticket"),
    path("flux/review/", views.create_review_and_ticket, name="review"),
    path("flux/review_response/<ticket_id>", views.create_review_response, name="review_response"),
    path("flux/posts/", views.posts, name="posts"),
    path("flux/subscription/", views.subscription, name="subscription"),
    path("flux/delete_subscription/", views.deleteSubscription, name="delete_subscription"),
    path("flux/posts/delete_ticket/<ticket_id>", views.deleteTicket, name="delete-ticket"),
    path("flux/posts/delete_review/<review_id>", views.deleteReview, name="delete-review")
]