# Generated by Django 5.0.3 on 2024-03-18 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_card_rarity_alter_priceupdate_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='image_url',
        ),
    ]