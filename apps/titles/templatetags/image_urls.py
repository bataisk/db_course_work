from django.template import Library


register = Library()
@register.filter(name='poster')
def get_poster_url(obj, size):
    return f'https://image.tmdb.org/t/p/{size}/{obj.poster_url}'


@register.filter(name='backdrop')
def get_backdrop_url(obj, size):
    return f'https://image.tmdb.org/t/p/{size}/{obj.backdrop_url}'


