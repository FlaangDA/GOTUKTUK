# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 11:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trip', '0002_auto_20160425_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickuppoint', models.CharField(default=b'0000.00000', max_length=25)),
                ('requestedprice', models.FloatField()),
                ('acceptedprice', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gtt_customer_triprequest', to=settings.AUTH_USER_MODEL)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gtt_driver_triprequest', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'TripRequest',
                'verbose_name_plural': 'TripRequests',
            },
        ),
    ]
