# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-24 06:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customerdetails',
            table='users_customerdetails',
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='users_customuser',
        ),
        migrations.AlterModelTable(
            name='driverdetails',
            table='users_driverdetails',
        ),
    ]
