import requests
import json


# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_movie_db.settings')
# import django
# django.setup()
#
#
from apps.people.models import Person
from apps.titles.models import Title
from django.core.exceptions import ObjectDoesNotExist


def get_data(target):
    api_key = 'api_key=5dafce136791e179e789af8a474d60a5'
    start_url = 'https://api.themoviedb.org/3'

    return json.loads(requests.get(url=f'{start_url}{target}?{api_key}').text)


def create_person(person_id):
    person_data = get_data(f'/person/{person_id}')

    try:
        Person.objects.get(tmdb_id=person_data['id'])
        return
    except ObjectDoesNotExist:
        pass

    person = Person()

    person.birthday = person_data['birthday']
    person.deathday = person_data['deathday']
    person.known_for = person_data['known_for_department']
    person.tmdb_id = person_data['id']
    person.imdb_id = person_data['imdb_id']
    person.name = person_data['name']
    person.biography = person_data['biography']
    person.popularity = person_data['popularity']
    person.photo = person_data['profile_path']

    person.save()


def get_related_to_title_people_ids(title_id, is_movie=True):
    if is_movie:
        title_credits = get_data(f'/movie/{title_id}/credits')
    else:
        title_credits = get_data(f'/tv/{title_id}/credits')

    cast = title_credits['cast']
    crew = title_credits['crew']

    return [item['id'] for item in cast], [item['id'] for item in crew]


def populate_people(titles, is_movies=True):
    for title in titles:
        cast, crew = get_related_to_title_people_ids(title.tmdb_id, is_movies)
        for person_id in cast:
            create_person(person_id)
        for person_id in crew:
            create_person(person_id)


if __name__ == '__main__':
    create_person(1830011)

populate_people(titles=Title.objects.filter(is_movie=True))

