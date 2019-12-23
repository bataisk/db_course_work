from django.shortcuts import render
from .models import Title, Image
from apps.people.models import CreatorRole, ActorRole


def title_page(request, title_id):
    title = Title.objects.get(pk=title_id)
    important_jobs = (
        'Producer',
        'Screenplay',
        'Director'
    )

    cast = ActorRole.objects.filter(title=title)[:5].prefetch_related('actor')

    raw_crew = CreatorRole.objects.filter(title=title).filter(job__in=important_jobs)[:9].prefetch_related('creator')
    cleaned_crew = []
    distinct_creators = set([creator.creator for creator in raw_crew])
    for distinct_creator in distinct_creators:
        cleaned_crew.append({
            'job': ', '.join([creator.job for creator in raw_crew if creator.creator == distinct_creator]),
            'creator': distinct_creator
        })

    genres = title.genres.all()

    posters = title.images.filter(is_poster=True)[:5]
    backdrops = title.images.filter(is_poster=False)[:5]

    context = {
        'title': title,
        'crew': cleaned_crew,
        'cast': cast,
        'genres': genres,
        'posters': posters,
        'posters_count': title.images.filter(is_poster=True).count(),
        'backdrops': backdrops,
        'backdrops_count': title.images.filter(is_poster=False).count()
    }

    return render(request, 'titles/title.html', context=context)
