from django.urls import path
from .views import discover_movies, discover_shows

urlpatterns = [
    path('movie/', discover_movies, name='discover_movie'),
    path('show/', discover_shows, name='discover_show')
]
