# Generated by Django 2.2.5 on 2019-12-23 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0004_auto_20191215_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='is_both_genre',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='is_movie_genre',
        ),
    ]
