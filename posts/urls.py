
from django.urls import path
from . import views


urlpatterns = [
    path("create-post/", views.post_create, name='create-post'),
] 