# Generated by Django 2.2.5 on 2019-11-14 23:40

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('titles', '0011_auto_20191115_0230'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Titles',
            new_name='Title',
        ),
    ]