from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters import OrderingFilter as o_filters
from .models import Genre, Staff, Movie


class GenreFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Genre
        fields = ["name"]


class StaffFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Staff
        fields = ["name"]


class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    actor_id = filters.NumberFilter(field_name="actors__id")
    director_id = filters.NumberFilter(field_name="director__id")
    genre_id = filters.NumberFilter(field_name="genre__id")
    overall_rating=filters.NumberFilter(field_name="movie_overall_rating")

    ordering = filters.OrderingFilter(
        fields={
            "release_date": "release_date",
            "title": "title",
        },
        label="Ordering by release_date, -release_date, title, or -title",
    )

    class Meta:
        model = Movie
        fields = ["title", "genre_id", "actor_id", "director_id", "overall_rating"]
