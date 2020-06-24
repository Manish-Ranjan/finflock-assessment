from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import MovieAPIView, RatingAPIView, MoviesAPIView
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
# router.register(r'^movie/', get_movies,basename="movie")
# router.register(r'rating/<int:pk>', RatingViewset,basename="rating")
urlpatterns = [
    path('movies/', MoviesAPIView.as_view(), name='movies'),
    path('movie/<int:pk>/', MovieAPIView.as_view(), name='movie'),
    path('rating/<int:pk>/', RatingAPIView.as_view(), name='rating'),

]
