# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-22 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0025_auto_20160919_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='triprequest',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
