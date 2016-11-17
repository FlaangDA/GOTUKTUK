from django.shortcuts import render

# Create your views here.
#Django packages
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View

#App
from models import PackageDeal
from forms import CreationFormPackageDeal

import json, simplejson

import logging
l = logging.getLogger('django.request')
l2 = logging.getLogger('default')

class PackagedealView(View):

	def get_packagedeals(self, request):
		return HttpResponse(serializers.serialize("json", PackageDeal.objects.all()))

	def create_packagedeal(self, request):

		json_data = json.loads(request.body)
		
		formDeal = CreationFormPackageDeal(json_data)
		pd = None
		l2.debug(formDeal)
		if formDeal.errors:
			l2.debug(formDeal.errors)
			
		if formDeal.is_valid():
			pd = PackageDeal.objects.create_packagedeal(json_data)

		return HttpResponse(pd, content_type="application/json")

	def post(self, request, *args, **kwargs):

		if request.path == '/create_packagedeal':
			return self.create_packagedeal(request)

	def get(self, request, *args, **kwargs):

		if request.path == '/get_packagedeals':
			return self.get_packagedeals(request)