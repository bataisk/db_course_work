from django.db import models


class Title(models.Model):
    is_movie = models.BooleanField(default=True)
    backdrop_url = models.CharField(max_length=50, null=True)
    poster_url = models.CharField(max_length=50, null=True)
    budget = models.IntegerField(null=True)
    homepage = models.URLField(null=True)
    imdb_id = models.CharField(max_length=9, null=True)
    tmdb_id = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    overview = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    release_date = models.DateField(null=True)
    revenue = models.IntegerField(null=True)
    runtime = models.IntegerField(null=True)
    status = models.CharField(max_length=20, null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(default=0)
    type = models.CharField(max_length=20, null=True)

    episode_runtime = models.IntegerField(null=True)
    number_of_episodes = models.IntegerField(default=1)
    number_of_seasons = models.IntegerField(default=1)
    last_air_date = models.DateField(null=True)

    def get_absolute_url(self):
        return f'/title/{self.pk}'

    class Meta:
        db_table = 'titles'


class Image(models.Model):
    is_poster = models.BooleanField(default=True)
    url = models.CharField(max_length=50)
    height = models.IntegerField()
    width = models.IntegerField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='images')

    class Meta:
        db_table = 'titles_images'


class Genre(models.Model):
    is_movie_genre = models.BooleanField(default=True)
    is_both_genre = models.BooleanField(default=False)
    name = models.CharField(max_length=20, unique=True)
    titles = models.ManyToManyField(Title, db_table='title_genre', related_name='genres')

    class Meta:
        db_table = 'genres'
        ordering = ('name',)




