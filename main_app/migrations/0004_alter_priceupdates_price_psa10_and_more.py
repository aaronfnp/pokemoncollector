# Generated by Django 5.0.3 on 2024-03-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_card_rarity_priceupdates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceupdates',
            name='price_psa10',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='priceupdates',
            name='price_ungraded',
            field=models.IntegerField(),
        ),
    ]
