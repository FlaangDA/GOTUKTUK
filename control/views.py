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
from users.models import CustomUser, CustomerDetails, DriverDetails
from users.forms import DriverDetailsChangeForm
from packagedeals import views, models


# Create your views here.


class AvailabilityView(View):

	model = DriverDetails
	fields = ['is_available']

	def enable_driver(self, user):
		try:
			driver = DriverDetails.objects.get(user_instance=user)
			driver.is_available = True
			driver.save()

			return HttpResponse("Driver was marked as is_available == True")
		except Exception:
			return HttpResponseBadRequest("Could not change is_available")

		return HttpResponse("Could not change is_available")

	def disable_driver(self, user):

		#Edit to use a form to change database entries
		try:
			
			driver = DriverDetails.objects.get(user_instance=user)
			driver.available = False
			driver.save()

			return HttpResponse("Driver was marked as is_available == True")
		except Exception:
			return HttpResponseBadRequest("Could not change is_available")

	def available_drivers(self, request):

		d = DriverDetails.objects.select_related('user_instance')

		obj_dict = dict([(obj.user_instance.email, [("lon", obj.lon), ("lat", obj.lat), ("phone", obj.phone), ("Available", obj.available)]) for obj in d if obj.available])

		return HttpResponse(json.dumps(obj_dict), content_type="application/json")

	def dummy(self, request):

		return HttpResponse("You entered the dummy GET_Request")

	def post(self, request, *args, **kwargs):

		user = CustomUser.objects.get(email=request.session['user_email'])

		if request.path == '/enable_driver/':
			return self.enable_driver(user)
		elif request.path == '/disable_driver/':
			return self.disable_driver(user)

		return HttpResponse("AvailabilityView POST unknown action")

	def get(self, request):

		if request.method == 'GET':
			if request.path == '/available_drivers/':
				return self.available_drivers(request)

class DriverListView(ListView):
	model = DriverDetails

class DriverDetailView(DetailView):
	model = DriverDetails

class CustomerDetailsView(DetailView):
	model = CustomerDetails

	def get_context_data(self, **kwargs):
		context = super(CustomerDetailsView, self).get_context_data(**kwargs)

		user = CustomUser.objects.get(email=kwargs.get('email'))

		context['user_instance'] = CustomerDetails.objects.select_related('user_instance').get(user_instance=user)