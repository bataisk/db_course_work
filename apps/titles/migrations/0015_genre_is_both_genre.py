# Generated by Django 2.2.5 on 2019-11-20 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0014_genre_is_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='is_both_genre',
            field=models.BooleanField(default=False),
        ),
    ]