# Generated by Django 2.2.5 on 2019-12-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0003_auto_20191212_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='titles',
            field=models.ManyToManyField(db_table='title_genre', related_name='genres', to='titles.Title'),
        ),
    ]
