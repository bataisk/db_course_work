from django.template import Library


register = Library()


@register.filter(name='poster')
def get_poster_url(obj, size):
    return f'https://image.tmdb.org/t/p/{size}/{obj.poster_url}'


@register.filter(name='backdrop')
def get_backdrop_url(obj, size):
    return f'https://image.tmdb.org/t/p/{size}/{obj.backdrop_url}'


@register.filter(name='photo')
def get_photo(obj, size):
    return f'https://image.tmdb.org/t/p/{size}/{obj.photo}'


@register.filter(name='image')
def get_photo(obj, size):
    return f'https://image.tmdb.org/t/p/{size}/{obj.url}'


