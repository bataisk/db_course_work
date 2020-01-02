from django.shortcuts import render
from django.db.models import Q
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


def get_filtered_query(is_movies_page=True, is_titles_page=False, release_year=None, sort_by=None, genres=None):
    f = Q()
    if not is_titles_page:
        f = Q(is_movie=is_movies_page)

    if release_year:
        f &= Q(release_date__year=release_year)

    if genres:
        f &= Q(genres__in=genres)

    if sort_by:
        return Title.objects.filter(f).order_by().order_by(sort_by)
    else:
        return Title.objects.filter(f)


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


def discover_page(request):
    if request.path.split('/')[2] == 'movie':
        is_movies_page = True
        is_titles_page = False
    elif request.path.split('/')[2] == 'title':
        is_titles_page = True
        is_movies_page = False
    else:
        is_movies_page = False
        is_titles_page = False

    titles_filters = {
        'is_movies_page': is_movies_page,
        'is_titles_page': is_titles_page,
        'release_year': None,
        'sort_by': '',
        'genres': []
    }

    try:
        titles_filters['release_year'] = int(request.GET.get('release-year'))
    except TypeError:
        pass

    try:
        titles_filters['sort_by'] = request.GET.get('sort-by')
    except TypeError:
        pass

    try:
        titles_filters['genres'] = request.GET.getlist('genres')
        titles_filters['genres'] = [int(i) for i in titles_filters['genres']]
    except TypeError:
        pass

    titles = get_filtered_query(**titles_filters)
    paginator = Paginator(titles, 10)

    try:
        page_number = int(request.GET.get('page'))
    except TypeError:
        page_number = 1

    movies = paginator.get_page(page_number)
    pages = set_up_pages(page_number, paginator.num_pages)
    years = list(range(1900, 2021))
    years.reverse()

    context = {
        'genres': Genre.objects.all(),
        'years': years,
        'results': movies,
        'pages': pages,
        'full_path': request.get_full_path(),
        'is_movies_page': is_movies_page,
        'is_titles_page': is_titles_page,
        'selected_values': titles_filters
    }
    return render(request, 'discover/discover.html', context=context)


def handler404(request, *args, **argv):
    return render(request, 'base/404.html')

# def discover_shows(request):
#     paginator = Paginator(Title.objects.filter(is_movie=False), 10)
#
#     try:
#         page_number = int(request.GET.get('page'))
#     except TypeError:
#         page_number = 1
#
#     shows = paginator.get_page(page_number)
#     pages = set_up_pages(page_number, paginator.num_pages)
#
#     years = list(range(1900, 2021))
#     years.reverse()
#
#     context = {
#         'genres': Genre.objects.all(),
#         'years': years,
#         'results': shows,
#         'pages': pages,
#         'is_movies_page': False
#     }
#
#     return render(request, 'discover/discover.html', context=context)

