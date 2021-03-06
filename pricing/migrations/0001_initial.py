# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afternoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('name', models.CharField(default='Afternoon base price', max_length=100)),
            ],
            options={
                'verbose_name': '12:00 AM - 2:00 PM Afternoon',
            },
        ),
        migrations.CreateModel(
            name='EarlyAfternoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('name', models.CharField(default='EarlyAfternoon base price', max_length=100)),
            ],
            options={
                'verbose_name': '2:00 PM - 5:00 PM Early afternoon',
            },
        ),
        migrations.CreateModel(
            name='EarlyMorning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('name', models.CharField(default='EarlyMorning base price', max_length=100)),
            ],
            options={
                'verbose_name': '6:00 AM - 8:00 AM Early morning',
            },
        ),
        migrations.CreateModel(
            name='Evening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('name', models.CharField(default='Evening base price', max_length=100)),
            ],
            options={
                'verbose_name': '6:00 PM - 8:00 PM Evening',
            },
        ),
        migrations.CreateModel(
            name='LateAfternoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('name', models.CharField(default='LateAfternoon base price', max_length=100)),
            ],
            options={
                'verbose_name': '5:00 PM - 6:00 PM Late afternoon',
            },
        ),
        migrations.CreateModel(
            name='Morning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('name', models.CharField(default='Morning base price', max_length=100)),
            ],
            options={
                'verbose_name': '8:00 PM - 12:00 AM Morning',
            },
        ),
        migrations.CreateModel(
            name='Nighttime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('name', models.CharField(default='Nighttime base price', max_length=100)),
            ],
            options={
                'verbose_name': '8:00 PM - 6:00 AM Nighttime',
            },
        ),
        migrations.CreateModel(
            name='AfternoonProfit',
            fields=[
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('nameProfit', models.CharField(default='Afternoon profit', max_length=100)),
                ('related', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pricing.Afternoon')),
            ],
            options={
                'verbose_name': 'Afternoon profits',
            },
        ),
        migrations.CreateModel(
            name='EarlyAfternoonProfit',
            fields=[
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('nameProfit', models.CharField(default='EarlyAfternoon profit', max_length=100)),
                ('related', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pricing.EarlyAfternoon')),
            ],
            options={
                'verbose_name': 'EarlyAfternoon profits',
            },
        ),
        migrations.CreateModel(
            name='EarlyMorningProfit',
            fields=[
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('nameProfit', models.CharField(default='EarlyMorning profit', max_length=100)),
                ('related', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pricing.EarlyMorning')),
            ],
            options={
                'verbose_name': 'EarlyMorning profitss',
            },
        ),
        migrations.CreateModel(
            name='EveningProfit',
            fields=[
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('nameProfit', models.CharField(default='Evening profit', max_length=100)),
                ('related', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pricing.Evening')),
            ],
            options={
                'verbose_name': 'Evening profits',
            },
        ),
        migrations.CreateModel(
            name='LateAfternoonProfit',
            fields=[
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('nameProfit', models.CharField(default='LateAfternoon profit', max_length=100)),
                ('related', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pricing.LateAfternoon')),
            ],
            options={
                'verbose_name': 'LateAfternoon profits',
            },
        ),
        migrations.CreateModel(
            name='MorningProfit',
            fields=[
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('nameProfit', models.CharField(default='Morning profit', max_length=100)),
                ('related', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pricing.Morning')),
            ],
            options={
                'verbose_name': 'Morning profits',
            },
        ),
        migrations.CreateModel(
            name='NighttimeProfit',
            fields=[
                ('usd1km', models.FloatField(default=2.0, verbose_name='1 km')),
                ('usd2km', models.FloatField(default=2.0, verbose_name='2 km')),
                ('usd3km', models.FloatField(default=3.0, verbose_name='3 km')),
                ('usd4km', models.FloatField(default=4.0, verbose_name='4 km')),
                ('usd5km', models.FloatField(default=5.0, verbose_name='5 km')),
                ('usd6km', models.FloatField(default=5.5, verbose_name='6 km')),
                ('usd7km', models.FloatField(default=6.5, verbose_name='7 km')),
                ('usd8km', models.FloatField(default=8.0, verbose_name='8 km')),
                ('usd9km', models.FloatField(default=12.0, verbose_name='9 km')),
                ('usd10km', models.FloatField(default=12.0, verbose_name='>= 10 km')),
                ('nameProfit', models.CharField(default='Nighttime profit', max_length=100)),
                ('related', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pricing.Nighttime')),
            ],
            options={
                'verbose_name': 'Nighttime profits',
            },
        ),
    ]
