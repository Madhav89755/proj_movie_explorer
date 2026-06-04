from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Movie, Genre, Staff
from .api_filter import GenreFilter, MovieFilter, StaffFilter
from .api_serializers import (
    GenreSerializer,
    StaffSerializer,
    MovieListSerializer,
    MovieDetailsSerializer,
    MovieCreateUpdateSerializer,
)

class MovieAPIView(ListAPIView):
    """APIView for listing all movies."""

    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filterset_class = MovieFilter

class MovieDetailAPIView(RetrieveAPIView):
    """APIView for retrieving a single movie."""

    queryset = Movie.objects.all()
    serializer_class = MovieDetailsSerializer

class MovieCreateUpdateDeleteAPIView(ModelViewSet):
    """APIView for creating, updating, and deleting movies."""

    queryset = Movie.objects.all()
    serializer_class = MovieCreateUpdateSerializer
    http_method_names = ["post", "patch", "delete", "head", "options"]

class GenreViewset(ModelViewSet):
    """Viewset for managing genres."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filterset_class = GenreFilter

class StaffViewset(ModelViewSet):
    """Viewset for managing staff members."""

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filterset_class = StaffFilter
