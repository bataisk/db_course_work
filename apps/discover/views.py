from django.shortcuts import render
from apps.titles.models import Title, Genre


def index(request):
    shows = Title.objects.filter(is_movie=False)[:3]
    movies = Title.objects.filter(is_movie=True)[:3]

    context = {
        'first_show': shows[0],
        'other_shows': shows[1:],
        'other_movies': movies[:2],
        'last_movie': movies[2]
    }

    return render(request, 'discover/index.html', context=context)


def discover_movies(request):
    movies = Title.objects.filter(is_movie=True)
    sql_query = 'SELECT * FROM genres WHERE is_movie_genre = TRUE OR is_both_genre = TRUE;'

    context = {
        'genres': Genre.objects.raw(sql_query),
        'years': list(range(1900, 2020)),
        'results': movies,
        'is_movies_page': True
    }
    return render(request, 'discover/discover.html', context=context)


def discover_shows(request):
    shows = Title.objects.filter(is_movie=False)
    sql_query = 'SELECT * FROM genres WHERE is_movie_genre = FALSE OR is_both_genre = TRUE;'

    context = {
        'genres': Genre.objects.raw(sql_query),
        'years': list(range(1900, 2020)),
        'results': shows,
        'is_movies_page': False
    }
    return render(request, 'discover/discover.html', context=context)

