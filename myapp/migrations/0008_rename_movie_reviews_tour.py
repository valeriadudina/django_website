# Generated by Django 4.1.7 on 2023-03-27 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_movie_tourshots_tour'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='movie',
            new_name='tour',
        ),
    ]