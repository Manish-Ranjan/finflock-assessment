from rest_framework import serializers
from .models import Movie, Rating


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'description', 'category', 'author'
        )


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'description', 'category', 'author'
        )
