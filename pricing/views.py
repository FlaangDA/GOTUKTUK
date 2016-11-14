from django.shortcuts import render
from models import EarlyMorning, Morning, Afternoon, EarlyAfternoon, LateAfternoon, Evening, Nighttime, EarlyMorningProfit, MorningProfit, AfternoonProfit, EarlyAfternoonProfit, LateAfternoonProfit, EveningProfit, NighttimeProfit
from datetime import datetime
# Create your views here.

def calculate_price(tripordertime, distanceKm):
	now = datetime.now()

	debtDict = {
			"customer_paid" : 10.0,
			"driver_owes" : 1.5,
		}

	nighttimeEarly = now.replace(hour = 6, minute = 0, second = 0, microsecond = 0)
	earlyMorning = now.replace(hour = 8, minute = 0, second = 0, microsecond = 0)
	morning = now.replace(hour = 12, minute = 0, second = 0, microsecond = 0)
	earlyafternoon = now.replace(hour = 14, minute = 0, second = 0, microsecond = 0)
	lateafternoon = now.replace(hour = 17, minute = 0, second = 0, microsecond = 0)
	evening = now.replace(hour = 18, minute = 0, second = 0, microsecond = 0)
	nighttimeLate = now.replace(hour = 23, minute = 59, second = 59, microsecond = 0)
	try:
		if tripordertime < nighttimeEarly:
			return get_price_by_km(Nighttime.objects.get(id=1), NighttimeProfit.objects.get(id=1), distanceKm)
		elif nighttimeEarly <= tripordertime < earlyMorning:
			return get_price_by_km(EarlyMorning.objects.get(id=1), EarlyMorningProfit.objects.get(id=1), distanceKm)
		elif earlyMorning <= tripordertime < morning:
			return get_price_by_km(Morning.objects.get(id=1), MorningProfit.objects.get(id=1), distanceKm)
		elif morning <= tripordertime < earlyafternoon:
			return get_price_by_km(EarlyAfternoon.objects.get(id=1), EarlyAfternoonProfit.objects.get(id=1), distanceKm)
		elif earlyafternoon <= tripordertime < lateafternoon:
			return get_price_by_km(LateAfternoon.objects.get(id=1), LateAfternoonProfit.objects.get(id=1), distanceKm)
		elif lateafternoon <= tripordertime < evening:
			return get_price_by_km(Evening.objects.get(id=1), EveningProfit.objects.get(id=1), distanceKm)
		elif evening <= tripordertime < nighttimeLate:
			return get_price_by_km(Nighttime.objects.get(id=1), NighttimeProfit.objects.get(id=1), distanceKm)
	
	except Exception as e:
		return debtDict
	return debtDict

def get_price_by_km(baseprice_obj, feeprice_obj, distanceKm):

	str_km = str(distanceKm) + " km"

	basefields = baseprice_obj.__dict__
	feefields = feeprice_obj.__dict__

	base = 0.0
	fee = 0.0

	for field, value in basefields.items():
		if field.verbose_name == str_km:
			fee = value
			break

	for field, value in feefields.items():
		if field.verbose_name == str_km:
			base = value
			break

	debtDict = {
		"customer_paid" : base + fee,
		"driver_owes" : fee
	}

	return debtDict


