# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-31 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0031_tripsession_tripgraphic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripsession',
            name='tripgraphic',
        ),
    ]
