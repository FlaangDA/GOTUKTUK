# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0036_tripsession_tripsessiongraphic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripsession',
            name='tripsessiongraphic',
            field=models.ImageField(default=b'tripsession/default.jpg', upload_to=b'tripsession/'),
        ),
    ]
