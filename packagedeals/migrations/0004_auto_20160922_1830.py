# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-22 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packagedeals', '0003_auto_20160919_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedeal',
            name='header_image',
            field=models.ImageField(default='packagedeals/headers/pin_location.png', upload_to='packagedeals/headers/'),
        ),
    ]
