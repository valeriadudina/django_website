# Generated by Django 4.1.7 on 2023-03-26 00:49

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_tour_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_client_trips',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='review',
            field=models.CharField(max_length=1000, verbose_name='Заполни форму ниже'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tinder',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tinder',
            name='person_details',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('smart', 'Умный'), ('funny', 'Веселый'), ('versatile', 'Разносторонний'), ('talkative', 'Общительный'), ('brave', 'Смелый')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='tinder',
            name='prefered_activities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('sea_activities', 'Загорать и купаться'), ('walking', 'Гулять по городу'), ('for_oldies', 'Посетить санаторий/спа'), ('mountains', 'Подняться в горы'), ('for_masha', 'Сходить в поход'), ('museums', 'Посещать музеи и достопримечательности'), ('sex', 'Развлекаться')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='tinder_review_2',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tourshots',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='type',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]