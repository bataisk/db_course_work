from django.shortcuts import render
from apps.titles.models import Title


def search_page(request):
    try:
        query = request.GET.get('query')
    except TypeError:
        query = ''

    if query:
        results = Title.objects.filter(name__icontains=query)
    else:
        results = []

    context = {
        'results': results,
        'query': query
    }

    return render(request, 'search/search.html', context=context)
