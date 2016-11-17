from django.shortcuts import render
from models import DebtTable
# Create your views here.

def payOffDebt(dd_obj, subtract_amount):
	table = DebtTable.objects.get(driver=dd_obj)
	table.debt -= subtract_amount
	table.save()

def addToDebt(dd_obj, add_amount):
	table = DebtTable.objects.get(driver=dd_obj)
	table.debt += add_amount
	table.save()