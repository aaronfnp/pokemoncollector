# Generated by Django 5.0.3 on 2024-03-15 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_priceupdates_price_psa10_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PriceUpdates',
            new_name='PriceUpdate',
        ),
    ]
