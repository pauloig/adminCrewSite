# Generated by Django 4.0.6 on 2024-07-16 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_locations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Locations',
            new_name='Location',
        ),
    ]
