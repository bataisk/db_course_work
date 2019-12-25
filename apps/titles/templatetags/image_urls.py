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


@register.filter(name='page_url')
def get_url(full_path, page):
    get_parameters = ''.join(full_path.split('/')[3:])
    get_parameters = get_parameters.split('&')
    if page in get_parameters:
        for parameter in get_parameters:
            if parameter.startswith('page='):
                parameter = f'page={page}'
                break
    else:
        get_parameters.append(f'page={page}')

    return '&'.join(get_parameters)

