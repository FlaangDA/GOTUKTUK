# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-22 10:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0016_auto_20160622_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='tripdate',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 10, 44, 29, 248343, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tripsession',
            name='tripenddatetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 10, 44, 29, 248998, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tripsession',
            name='triporderdatetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 10, 44, 29, 248961, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tripsession',
            name='tripstartdatetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 10, 44, 29, 248980, tzinfo=utc)),
        ),
    ]
