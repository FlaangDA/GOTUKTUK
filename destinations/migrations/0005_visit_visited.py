# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-04 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0004_auto_20161003_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='visited',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]