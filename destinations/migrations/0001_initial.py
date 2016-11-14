# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-18 13:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lon', models.CharField(default='0000.00000', max_length=10)),
                ('lat', models.CharField(default='0000.00000', max_length=10)),
                ('name', models.CharField(default='destination_name', max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Destination',
                'verbose_name_plural': 'Destinations',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.Destination')),
            ],
        ),
    ]
