# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-26 06:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160625_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='user_instance',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gtt_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='driverdetails',
            name='user_instance',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gtt_driver', to=settings.AUTH_USER_MODEL),
        ),
    ]
