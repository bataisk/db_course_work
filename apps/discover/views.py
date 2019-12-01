from django.shortcuts import render
from apps.titles.models import Title, Genre
from django.core.paginator import Paginator


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


def rate_in_percents(rate):
    return str(rate * 10)[:2]


def set_up_pages(page_number, pages_number):
    pages = {
         'is_next_exist': False,
         'is_previous_exist': False,
         'is_fists_exist': False,
         'is_lasts_exist': False,
         'previous_pages': [],
    }

    if page_number != pages_number:
        pages['is_next_exist'] = True
        pages['next'] = page_number + 1

    if page_number != 1:
        pages['is_previous_exist'] = True
        pages['previous_page'] = page_number - 1

        for i in range((page_number - 3) if page_number - 3 >= 1 else 1, page_number):
            pages['previous_pages'].append(i)

    if page_number >= 7:
        pages['is_fists_exist'] = True
    if page_number <= pages_number:
        pages['next_pages'] = []
        for i in range(page_number + 1, (page_number + 4) if page_number + 3 <= pages_number else pages_number + 1):
            pages['next_pages'].append(i)

    if page_number + 7 <= pages_number:
        pages['is_lasts_exist'] = True
        pages['last'] = (pages_number - 1, pages_number)

    return pages


def discover_movies(request):
    sql_query = 'SELECT * FROM genres WHERE is_movie_genre = TRUE OR is_both_genre = TRUE;'
    paginator = Paginator(Title.objects.filter(is_movie=True), 10)

    try:
        page_number = int(request.GET.get('page'))
    except TypeError:
        page_number = 1

    movies = paginator.get_page(page_number)
    pages = set_up_pages(page_number, paginator.num_pages)

    context = {
        'genres': Genre.objects.raw(sql_query),
        'years': list(range(1900, 2020)).reverse(),
        'results': movies,
        'pages': pages,
        'is_movies_page': True
    }
    return render(request, 'discover/discover.html', context=context)


def discover_shows(request):
    paginator = Paginator(Title.objects.filter(is_movie=False), 10)
    sql_query = 'SELECT * FROM genres WHERE is_movie_genre = FALSE OR is_both_genre = TRUE;'

    try:
        page_number = int(request.GET.get('page'))
    except TypeError:
        page_number = 1

    shows = paginator.get_page(page_number)
    pages = set_up_pages(page_number, paginator.num_pages)



    context = {
        'genres': Genre.objects.raw(sql_query),
        'years': list(range(1900, 2020)).reverse(),
        'results': shows,
        'pages': pages,
        'is_movies_page': False
    }
    return render(request, 'discover/discover.html', context=context)

