from django.shortcuts import render
from titles.models import Titles


def index(request):
    shows = Titles.objects.filter(is_movie=False)[:3]
    movies = Titles.objects.filter(is_movie=True)[:3]

    context = {
        'first_show': shows[0],
        'other_shows': shows[1:],
        'other_movies': movies[:2],
        'last_movie': movies[2]
    }

    return render(request, 'discover/index.html', context=context)
