# Generated by Django 2.2.5 on 2019-11-20 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0013_remove_title_recommendations'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='is_movie_genre',
            field=models.BooleanField(default=True),
        ),
    ]