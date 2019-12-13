import requests
import json


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_movie_db.settings')
import django
django.setup()
from apps.titles.models import Genre, Title, Image
from django.core.exceptions import ObjectDoesNotExist


def get_data(target):
    api_key = 'api_key=5dafce136791e179e789af8a474d60a5'
    start_url = 'https://api.themoviedb.org/3'

    return json.loads(requests.get(url=f'{start_url}{target}?{api_key}').text)


def add_images_to_title(title_id, is_movie):
    if is_movie:
        data = get_data(f'/movie/{title_id}/images')
    else:
        data = get_data(f'/tv/{title_id}/images')

    posters = data['posters']
    backdrops = data['backdrops']

    for poster in posters:
        try:
            Image.objects.get(url=poster['file_path'])
        except ObjectDoesNotExist:
            img = Image()
            img.height = poster['height']
            img.width = poster['width']
            img.url = poster['file_path']
            img.is_poster = True
            img.vote_average = poster['vote_average']
            img.vote_count = poster['vote_count']
            img.title = Title.objects.get(tmdb_id__exact=title_id)
            img.save()

    for backdrop in backdrops:
        try:
            Image.objects.get(url=backdrop['file_path'])
        except ObjectDoesNotExist:
            img = Image()
            img.height = backdrop['height']
            img.width = backdrop['width']
            img.url = backdrop['file_path']
            img.is_poster = False
            img.vote_average = backdrop['vote_average']
            img.vote_count = backdrop['vote_count']
            img.title = Title.objects.get(tmdb_id__exact=title_id)
            img.save()


for show in Title.objects.filter(is_movie=False):
    add_images_to_title(show.tmdb_id, False)



# id_list = [i['id'] for i in get_data('/tv/on_the_air')['results']]

# for id_ in id_list:
#     data = get_data(f'/tv/{id_}')
#     title = Titles()
#     title.backdrop_url = data.get('backdrop_path')
#     title.homepage = data.get('homepage')
#     title.imdb_id = data.get('imdb_id')
#     title.tmdb_id = id_
#
#     title.overview = data.get('overview')
#     title.popularity = data.get('popularity')
#     title.poster_url = data.get('poster_path')
#     title.release_date = data.get('first_air_date')
#     title.runtime = data.get('runtime')
#     title.status = data.get('status')
#     title.name = data.get('name')
#     title.vote_average = data.get('vote_average')
#     title.vote_count = data.get('vote_count')
#     title.revenue = data.get('revenue')
#     title.budget = data.get('budget')
#
#     title.episode_runtime = data.get('episode_run_time')[0]
#     title.number_of_episodes = data.get('number_of_episodes')
#     title.number_of_seasons = data.get('number_of_seasons')
#     title.type = data.get('type')
#     title.is_movie = False
#
#     title.save()
#     for i in data.get('genres', ()):
#         genre = Genres.objects.get(name=i['name'])
#         genre.titles.add(title)























