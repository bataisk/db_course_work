from django.urls import path
from .views import discover_movies, discover_shows

urlpatterns = [
    path('movies/', discover_movies),
    path('shows/', discover_shows)
]