# Generated by Django 4.0.6 on 2024-08-07 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_location_locationid'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_hr',
            field=models.BooleanField(default=False),
        ),
    ]
