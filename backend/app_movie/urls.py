from django.urls import path
from rest_framework.routers import DefaultRouter

from .apis import MovieAPIView, MovieDetailAPIView

urlpatterns = [
    path("movies/", MovieAPIView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailAPIView.as_view(), name="movie-detail"),
]
