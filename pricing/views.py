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

	nighttimeEarly = now.replace(hour = 6, minute = 0, second = 0, microsecond = 0).time()
	earlyMorning = now.replace(hour = 8, minute = 0, second = 0, microsecond = 0).time()
	morning = now.replace(hour = 12, minute = 0, second = 0, microsecond = 0).time()
	afternoon = now.replace(hour = 14, minute = 0, second = 0, microsecond = 0).time()
	earlyafternoon = now.replace(hour = 17, minute = 0, second = 0, microsecond = 0).time()
	lateafternoon = now.replace(hour = 18, minute = 0, second = 0, microsecond = 0).time()
	evening = now.replace(hour = 20, minute = 0, second = 0, microsecond = 0).time()
	nighttimeLate = now.replace(hour = 23, minute = 59, second = 59, microsecond = 0).time()
	print tripordertime, morning <= tripordertime < earlyafternoon
	try:
		if tripordertime < nighttimeEarly:
			base = Nighttime.objects.get(name="Nighttime")
			return get_price_by_km(base, NighttimeProfit.objects.get(nameProfit="Nighttime"), distanceKm)
		elif nighttimeEarly <= tripordertime < earlyMorning:
			base = EarlyMorning.objects.get(name="EarlyMorning")
			return get_price_by_km(base, EarlyMorningProfit.objects.get(nameProfit="EarlyMorning"), distanceKm)
		elif earlyMorning <= tripordertime < morning:
			base = Morning.objects.get(name="Morning")
			return get_price_by_km(base, MorningProfit.objects.get(nameProfit="Morning"), distanceKm)
		elif afternoon <= tripordertime < earlyafternoon:
			base = EarlyAfternoon.objects.get(name="EarlyAfternoon")
			return get_price_by_km(base, EarlyAfternoonProfit.objects.get(nameProfit="EarlyAfternoon"), distanceKm)
		elif earlyafternoon <= tripordertime < lateafternoon:
			base = LateAfternoon.objects.get(name="LateAfternoon")
			return get_price_by_km(base, LateAfternoonProfit.objects.get(nameProfit="LateAfternoon"), distanceKm)
		elif lateafternoon <= tripordertime < evening:
			base = Evening.objects.get(name="Evening")
			return get_price_by_km(base, Evening.objects.get(nameProfit="Evening"), distanceKm)
		elif evening <= tripordertime < nighttimeLate:
			base = Nighttime.objects.get(name="Nighttime")
			return get_price_by_km(base, NighttimeProfit.objects.get(nameProfit="Nighttime"), distanceKm)
	
	except Exception as e:
		print e
	print "no if test hit"
	return debtDict

def get_price_by_km(baseprice_obj, feeprice_obj, distanceKm):

	if distanceKm > 10:
		distanceKm = 10
	str_km = str(distanceKm) + "km"

	basefields = baseprice_obj.__dict__
	feefields = feeprice_obj.__dict__

	base = 0.0
	fee = 0.0

	for field, value in basefields.items():
		print field, value
		if field[3:] == str_km:
			fee = value
			break

	for field, value in feefields.items():
		print field, value
		if field[3:] == str_km:
			base = value
			break

	debtDict = {
		"customer_paid" : base + fee,
		"driver_owes" : fee
	}

	return debtDict


