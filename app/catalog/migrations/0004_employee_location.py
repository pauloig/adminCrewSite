# Generated by Django 4.0.6 on 2024-07-16 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_locations_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.location'),
        ),
    ]