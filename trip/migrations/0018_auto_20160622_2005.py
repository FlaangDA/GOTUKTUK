# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-22 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0017_auto_20160622_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='tripdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tripsession',
            name='tripenddatetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tripsession',
            name='triporderdatetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tripsession',
            name='tripstartdatetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]