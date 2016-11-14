# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 13:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0012_auto_20160524_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='tripdate',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 25, 13, 9, 8, 715950, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='tripsession',
            name='tripenddatetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 25, 13, 9, 8, 716494, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tripsession',
            name='triporderdatetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 25, 13, 9, 8, 716459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tripsession',
            name='tripstartdatetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 25, 13, 9, 8, 716479, tzinfo=utc)),
        ),
    ]
