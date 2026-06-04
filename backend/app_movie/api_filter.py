from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Genre, Staff, Movie


class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    actor_name = filters.CharFilter(field_name="actors__name", lookup_expr="icontains")
    director_name = filters.CharFilter(
        field_name="director__name", lookup_expr="icontains"
    )
    genre_name = filters.CharFilter(field_name="genre__name", lookup_expr="icontains")

    class Meta:
        model = Movie
        fields = ["title", "genre_name", "actor_name", "director_name"]
