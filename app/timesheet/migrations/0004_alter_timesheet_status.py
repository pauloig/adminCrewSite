# Generated by Django 4.0.6 on 2024-07-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0003_rename_timesheetcontrol_timesheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='Status',
            field=models.IntegerField(choices=[(1, 'Draft'), (2, 'Sent'), (3, 'Pending'), (4, 'Aproved'), (5, 'Rejected')], default=1),
        ),
    ]
