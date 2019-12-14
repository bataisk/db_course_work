from django.db import models
from apps.titles.models import Title

# Create your models here.


class Person(models.Model):
    birthday = models.DateField(null=True, blank=True)
    deathday = models.DateField(null=True, blank=True)
    known_for = models.CharField(max_length=30, null=True, blank=True)
    tmdb_id = models.IntegerField()
    imdb_id = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=50)
    popularity = models.FloatField(null=True)
    biography = models.TextField(blank=True, default="")
    photo = models.URLField(null=True)

    works = models.ManyToManyField(Title, through='CreatorRole', related_name='crew')
    acting = models.ManyToManyField(Title, through='ActorRole', related_name='cast')

    class Meta:
        db_table = 'people'
        ordering = ['-popularity']


class ActorRole(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    actor = models.ForeignKey(Person, on_delete=models.CASCADE)
    character = models.CharField(max_length=100)

    class Meta:
        db_table = 'actor_role'
        unique_together = ('title', 'actor', 'character')


class CreatorRole(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    creator = models.ForeignKey(Person, on_delete=models.CASCADE)
    job = models.CharField(max_length=50)

    class Meta:
        db_table = 'creator_role'
        unique_together = ('title', 'creator', 'job')


