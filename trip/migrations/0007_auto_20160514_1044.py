# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 10:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0006_auto_20160514_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripsession',
            name='triporderdatetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 14, 10, 44, 26, 590901, tzinfo=utc)),
        ),
    ]
