import requests
import json


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_movie_db.settings')
import django
django.setup()
from apps.titles.models import Genre
from django.core.exceptions import ObjectDoesNotExist


def get_data(target):
    api_key = 'api_key=5dafce136791e179e789af8a474d60a5'
    start_url = 'https://api.themoviedb.org/3'

    return json.loads(requests.get(url=f'{start_url}{target}?{api_key}').text)


if __name__ == '__main__':
    for genre in get_data('/genre/tv/list')['genres']:
        try:
            g = Genre.objects.get(name__exact=genre['name'])
        except ObjectDoesNotExist:
            g = Genre(name=genre['name'])
            g.is_movie_genre = False
            g.save()


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























