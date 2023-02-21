from django.urls import path
from flux import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("flux/", views.flux, name="flux"),
    path("flux/ticket/", views.create_ticket, name="ticket"),
    path("flux/review/", views.create_review_and_ticket, name="review"),
    path("flux/review_response/", views.create_review_response, name="review_response")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
