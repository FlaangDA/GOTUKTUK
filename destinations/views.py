import json

# Django packages
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

# App imports
from packagedeals.models import CustomUser, CustomerDetails, DriverDetails
from packagedeals.forms import CreationFormPackageDeal
from packagedeals import views, models
from models import Destination
from forms import CreationFormDestiation

# Create your views here.


class DestinationView(View):


	def create_destination(self, request):

		form = CreationFormDestiation(data=request.POST)

		destination = None

		if form.is_valid():
			destination = Destination.objects.create_destination(request.POST)

		return HttpResponse(destination, content_type="application/json")

	def post(self, request, *args, **kwargs):
		
		if request.user.is_authenticated():
			if request.path == '/create_destination/':
				return self.create_destination(request)

