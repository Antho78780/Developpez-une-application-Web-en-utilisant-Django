from django.urls import path
from posts import views
urlpatterns = [
    path("flux/posts/", views.posts , name="posts")
]