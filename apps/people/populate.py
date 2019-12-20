import requests
import json
from apps.people.models import Person, Title, CreatorRole, ActorRole
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError


def get_data(target):
    api_key = 'api_key=5dafce136791e179e789af8a474d60a5'
    start_url = 'https://api.themoviedb.org/3'
    try:
        response = requests.get(url=f'{start_url}{target}?{api_key}')
        if response.ok:
            data = json.loads(response.text)
        else:
            data = dict()
    except:
        data = dict()
        print(f'Request error on target: {target}')
    return data


def create_person(person_id):
    person_data = get_data(f'/person/{person_id}')

    if not person_data:
        return

    try:
        Person.objects.get(tmdb_id=person_data['id'])
        print('exs', end='')
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
    print('new', end='')


def get_related_to_title_people_ids(title_id, is_movie=True):
    if is_movie:
        title_credits = get_data(f'/movie/{title_id}/credits')
    else:
        title_credits = get_data(f'/tv/{title_id}/credits')

    if not title_credits:
        return []

    cast = title_credits['cast']
    crew = title_credits['crew']

    return [item['id'] for item in cast] + [item['id'] for item in crew]


def populate_people(titles, is_movies=True):
    for title in titles:
        related_people_ids = get_related_to_title_people_ids(title.tmdb_id, is_movies)
        print(f'Creating people related {title.name}, {title.tmdb_id}. Number to create: {len(related_people_ids)}')
        for i, person_id in enumerate(related_people_ids):
            create_person(person_id)
            print(f' {i},', end='')

        print(f'Created all people related to title with name: {title.name}, tmdb_id: {title.tmdb_id}')


def populate_people_title_relations(title):
    if title.is_movie:
        people_data = get_data(f'/movie/{title.tmdb_id}/credits')
    else:
        people_data = get_data(f'/tv/{title.tmdb_id}/credits')

    print(f'Title {title.name}, {title.tmdb_id}, len of cast {len(people_data["cast"])}')
    for i, actor in enumerate(people_data['cast']):
        try:
            person = Person.objects.get(tmdb_id__exact=actor['id'])
        except ObjectDoesNotExist:
            print(f'\nPerson with tmdb_id: {actor["id"]}, name {actor["name"]} not exist, title_id: {title.tmdb_id}')
            continue

        try:
            ActorRole.objects.create(character=actor['character'], title=title, actor=person)
            print(f' new {i},')
        except IntegrityError:
            print(f' exs {i},')

    print(f'Title {title.name}, {title.tmdb_id}, len of crew {len(people_data["crew"])}')
    for i, creator in enumerate(people_data['crew']):
        try:
            person = Person.objects.get(tmdb_id__exact=creator['id'])
        except ObjectDoesNotExist:
            print(f'\nPerson with tmdb_id: {creator["id"]}, name {creator["name"]} not exist, title_id: {title.tmdb_id}')
            continue

        try:
            CreatorRole.objects.create(job=creator['job'], title=title, creator=person)
            print(f' new {i},')
        except IntegrityError:
            print(f' exs {i},')


for title in Title.objects.all():
    populate_people_title_relations(title)

