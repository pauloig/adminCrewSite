# Generated by Django 4.0.6 on 2024-06-25 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeID', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_initial', models.CharField(blank=True, max_length=100, null=True)),
                ('termination_date', models.CharField(blank=True, max_length=200, null=True)),
                ('hire_created', models.CharField(blank=True, max_length=200, null=True)),
                ('hourly_rate', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_supervisor', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
