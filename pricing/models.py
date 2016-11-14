from __future__ import unicode_literals

from django.db import models

# Create your models here.

"""
Description of how the pricing is organized

	A day is split into 7 different time periods, each represented by a model. 

		Early morning: 06:00 AM - 08:00 PM
		Morning: 08:00AM - 12:00AM
		Afternoon: 12:00AM - 2:00PM
		EarlyAfternoon: 2:00PM - 5:00PM
		LateAfternoon: 5:00PM - 6:00PM
		Evening: 6:00PM - 8:00PM
		Nighttime: 8:00PM - 06:00PM

	The different time periods have either Normal hours or Peak hours.

	The different time periods should inherit from an abtract base model.

"""

class BasePricing(models.Model):


	usd1km = models.FloatField(default=2.0, verbose_name="1 km")
	usd2km = models.FloatField(default=2.0, verbose_name="2 km")
	usd3km = models.FloatField(default=3.0, verbose_name="3 km")
	usd4km = models.FloatField(default=4.0, verbose_name="4 km")
	usd5km = models.FloatField(default=5.0, verbose_name="5 km")
	usd6km = models.FloatField(default=5.5, verbose_name="6 km")
	usd7km = models.FloatField(default=6.5, verbose_name="7 km")
	usd8km = models.FloatField(default=8.0, verbose_name="8 km")
	usd9km = models.FloatField(default=12.0, verbose_name="9 km")
	usd10km = models.FloatField(default=12.0, verbose_name=">= 10 km")

	class Meta:
		abstract = True



class EarlyMorning(BasePricing):
	name = models.CharField(max_length=100, default="EarlyMorning base price")

	class Meta:
		verbose_name = "6:00 AM - 8:00 AM Early morning"

class EarlyMorningProfit(EarlyMorning):
	nameProfit = models.CharField(max_length=100, default="EarlyMorning profit")

	class Meta:
		verbose_name = "EarlyMorning profitss"

class Morning(BasePricing):
	name = models.CharField(max_length=100, default="Morning base price")

	class Meta:
		verbose_name = "8:00 PM - 12:00 AM Morning"

class MorningProfit(Morning):
	nameProfit = models.CharField(max_length=100, default="Morning profit")

	class Meta:
		verbose_name = "Morning profits"

class Afternoon(BasePricing):
	name = models.CharField(max_length=100, default="Afternoon base price")

	class Meta:
		verbose_name = "12:00 AM - 2:00 PM Afternoon"

class AfternoonProfit(Afternoon):
	nameProfit = models.CharField(max_length=100, default="Afternoon profit")

	class Meta:
		verbose_name = "Afternoon profits"

class EarlyAfternoon(BasePricing):
	name = models.CharField(max_length=100, default="EarlyAfternoon base price")

	class Meta:
		verbose_name = "2:00 PM - 5:00 PM Early afternoon"

class EarlyAfternoonProfit(EarlyAfternoon):
	nameProfit = models.CharField(max_length=100, default="EarlyAfternoon profit")

	class Meta:
		verbose_name = "EarlyAfternoon profits"

class LateAfternoon(BasePricing):
	name = models.CharField(max_length=100, default="LateAfternoon base price")

	class Meta:
		verbose_name = "5:00 PM - 6:00 PM Late afternoon"

class LateAfternoonProfit(LateAfternoon):
	nameProfit = models.CharField(max_length=100, default="LateAfternoon profit")

	class Meta:
		verbose_name = "LateAfternoon profits"

class Evening(BasePricing):
	name = models.CharField(max_length=100, default="Evening base price")

	class Meta:
		verbose_name = "6:00 PM - 8:00 PM Evening"

class EveningProfit(Evening):
	nameProfit = models.CharField(max_length=100, default="Evening profit")

	class Meta:
		verbose_name = "Evening profits"

class Nighttime(BasePricing):
	name = models.CharField(max_length=100, default="Nighttime base price")

	class Meta:
		verbose_name = "8:00 PM - 6:00 AM Nighttime"

class NighttimeProfit(Nighttime):
	nameProfit = models.CharField(max_length=100, default="Nighttime profit")

	class Meta:
		verbose_name = "Nighttime profits"










