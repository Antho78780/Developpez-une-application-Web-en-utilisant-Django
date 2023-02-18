from django.urls import path
from flux import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("flux/", views.flux, name="flux"),
    path("flux/create_ticket/", views.create_ticket, name="ticket"),
    path("flux/create_review/", views.create_review, name="review")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
