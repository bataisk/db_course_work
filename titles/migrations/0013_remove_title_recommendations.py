# Generated by Django 2.2.5 on 2019-11-18 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0012_auto_20191115_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='recommendations',
        ),
    ]
