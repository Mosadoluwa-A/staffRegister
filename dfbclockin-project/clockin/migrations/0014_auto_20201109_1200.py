# Generated by Django 3.1.2 on 2020-11-09 11:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0001_initial'),
        ('clockin', '0013_auto_20201107_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='clockin',
            name='day',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='day.day'),
        ),
        migrations.AlterField(
            model_name='clockin',
            name='time_in',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 11, 9, 12, 0, 45, 626092), null=True),
        ),
    ]
