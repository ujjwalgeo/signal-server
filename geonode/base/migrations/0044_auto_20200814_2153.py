# Generated by Django 2.2.11 on 2020-08-14 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0043_auto_20200527_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hierarchicalkeyword',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='hierarchicalkeyword',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Slug'),
        ),
    ]
