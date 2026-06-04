from rest_framework import serializers
from .models import Movie, Genre, Staff

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ["id", "name"]


class MovieReadOnlySerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    actors = StaffSerializer(many=True, read_only=True)
    director = StaffSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = "__all__"