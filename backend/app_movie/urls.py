from django.urls import path
from rest_framework.routers import DefaultRouter

from .apis import (
    GenreViewset,
    MovieAPIView,
    MovieDetailAPIView,
    StaffViewset,
    MovieCreateUpdateDeleteAPIView,
)

router = DefaultRouter()
router.register(r"genres", GenreViewset, basename="genre")
router.register(r"staff", StaffViewset, basename="staff")
router.register(
    r"movies/manage", MovieCreateUpdateDeleteAPIView, basename="movie-manage"
)

urlpatterns = [
    path("movies/", MovieAPIView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailAPIView.as_view(), name="movie-detail"),
] + router.urls
