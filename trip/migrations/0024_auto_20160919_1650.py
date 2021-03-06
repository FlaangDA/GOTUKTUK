# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-19 16:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0023_auto_20160918_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='triprequest',
            name='tripcompleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='triprequest',
            name='driver',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='gtt_driver_triprequest', to=settings.AUTH_USER_MODEL),
        ),
    ]
