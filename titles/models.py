from django.db import models


class Titles(models.Model):
    backdrop_url = models.CharField(max_length=50, null=True)
    poster_url = models.CharField(max_length=50, null=True)
    budget = models.IntegerField(null=True)
    homepage = models.URLField(null=True)
    imdb_id = models.CharField(max_length=9)
    name = models.CharField(max_length=50)
    overview = models.TextField(null=True)
    popularity = models.IntegerField(null=True)
    release_date = models.DateField()
    revenue = models.IntegerField(null=True)
    runtime = models.DurationField(null=True)
    status = models.CharField(max_length=20, null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(default=0)
    type = models.CharField(max_length=20, null=True)

    episode_runtime = models.DurationField(null=True)
    number_of_episodes = models.IntegerField(default=1)
    number_of_seasons = models.IntegerField(default=1)
    last_air_date = models.DateField(null=True)

    recommendations = models.ManyToManyField('self', null=True)


class Genres(models.Model):
    name = models.CharField(max_length=20)
    titles = models.ManyToManyField(Titles)




