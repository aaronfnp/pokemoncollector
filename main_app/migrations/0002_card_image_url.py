# Generated by Django 5.0.3 on 2024-03-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image_url',
            field=models.URLField(default='https://commondatastorage.googleapis.com/images.pricecharting.com/refe27360bddc90f3ff8beb22b1a6fe2e243ad1ce704e20972a6af8b48aaadede8c/240.jpg'),
        ),
    ]
