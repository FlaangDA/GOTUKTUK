# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packagedeals', '0004_auto_20160922_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedeal',
            name='header_image',
            field=models.ImageField(default='packagedeals/headers/pin_location.png', upload_to='/Users/tormodfladby/Documents/TorgeirsArbeid/GOtuk/media/packagedeals/headers/'),
        ),
    ]