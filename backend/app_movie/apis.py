from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
# Create your views here.

from .models import Movie
from .api_filter import MovieFilter
from .api_serializers import MovieReadOnlySerializer

class MovieAPIView(ListAPIView):
    """APIView for listing all movies."""

    queryset = Movie.objects.all()
    serializer_class = MovieReadOnlySerializer
    filterset_class = MovieFilter

class MovieDetailAPIView(RetrieveAPIView):
    """APIView for retrieving a single movie."""

    queryset = Movie.objects.all()
    serializer_class = MovieReadOnlySerializer
    filterset_class = MovieFilter
