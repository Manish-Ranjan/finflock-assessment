from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import MovieSerializer, RatingSerializer,MoviesSerializer
from .models import Movie, Rating


class MoviesAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer


class MovieAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
