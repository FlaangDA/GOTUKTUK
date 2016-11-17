import json
from base64 import b64decode

# Django packages
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseBadRequest
from django.db import connection, transaction
from django.core.files.base import ContentFile

#Auth and register
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from forms.register import RegistrationFormCustomer, RegistrationFormDriver, RegistrationFormCustomerDetails, RegistrationFormDriverDetails
from forms.authenticate import AuthenticationForm
from forms.forms import DriverDetailsChangeForm, CustomerDetailsChangeForm
from backends import EmailAuthBackend
from debtcollector.models import DebtTable

#logging
import logging
l = logging.getLogger('django.request')
l2 = logging.getLogger('default')
from models import CustomUser, CustomerDetails, DriverDetails
from itertools import chain
# Create your views here.

class CreationView(View):

	customerForm = RegistrationFormCustomer
	customerDetailsForm = RegistrationFormCustomerDetails
	driverForm = RegistrationFormDriver
	driverDetailsForm = RegistrationFormDriverDetails

	@csrf_exempt
	def create_customer(self, request, user):
		json_data = json.loads(request.body)
		detailsForm = RegistrationFormCustomerDetails(json_data)

		if detailsForm.is_valid():
			cd = CustomerDetails.objects.create_customer_details(user=user, 
				phone=json_data.get('phone'), 
				facebookurl=json_data.get('facebookurl'), 
				nationality=json_data.get('nationality'))
			cd.save()

		return HttpResponse(user, content_type="application/json")

	def create_driver(self, request, user):

		json_data = json.loads(request.body)

		detailsForm = RegistrationFormDriverDetails(json_data)

		if detailsForm.is_valid():
			dd = DriverDetails.objects.create_driver_details(user=user, phone=json_data.get('phone'), facebookurl=json_data.get('facebookurl'))
			dd.save()
			driver_name = user.firstname + " " + user.lastname
			debt = DebtTable(driver = dd, debt = 0.0, driver_email=user.email, driver_name=driver_name)
			debt.save()

		return HttpResponse(user, content_type="application/json")
		
	@csrf_exempt
	def post(self, request, *args, **kwargs):
		l.debug(request)
		l2.error(request)
		l2.error(request.body)
		if request.path == '/create_customer':
			form = self.customerForm(json.loads(request.body))
			if form.is_valid():
				user = form.save()
				return self.create_customer(request, user)
			l2.error(form)
			return HttpResponseBadRequest("Customer form is not valid.")

		if request.path == '/create_driver':
			form = self.driverForm(json.loads(request.body))
			if form.is_valid():
				user = form.save()
				return self.create_driver(request, user)
			l2.error(form)
			return HttpResponseBadRequest("Driver form is not valid.")
		return HttpResponseBadRequest("Invalid URL")

class AuthView(View):

	def login(self, request):

		"""
		Duplicate sessions might occur when a user attempts to log in multiple times.
		Check if user is already logged in before logging the user in.
		"""

		json_data = json.loads(request.body)

		username = json_data.get('email')
		password = json_data.get('password')
		form = AuthenticationForm(json_data)


		if form.is_valid():

			try:
				user = authenticate(email=username, password=password)
				if user.is_authenticated():
					request.session['user_email'] = username
					if user.is_active:
						django_login(request, user)
						return HttpResponse("User is now logged in.")
					else:
						return HttpResponse("Inactive user.")
				else:
					return HttpResponse("User is None.(views.login())")
			except Exception:
				return HttpResponseBadRequest

		return HttpResponseBadRequest("User form invalid")

	def logout(self, request):

		json_data = json.loads(request.body)

		user = request.user

		if user.user_type == 'D':
			driver_instance = DriverDetails.objects.get(user_instance=user)

		try:
			django_logout(request)
			if user.user_type == 'D':
				driver_instance.available=False

			return HttpResponse("User logged out.")
		except Exception, e:
			raise e

		return HttpResponseBadRequest

	def post(self, request, *args, **kwargs):

		if request.path == '/login':
			return self.login(request)
		elif request.path == '/logout':
			return self.logout(request)
		return Http404("url does not exist")

class DetailsView(View):

	def add_profile_pic(self, request, details_obj):

		try:
			json_data = json.loads(request.body)

			base64raw = json_data.get('profile_pic')
			image_name = str(request.user.id) + "_profile.png"
			image_data = ContentFile(b64decode(base64raw), image_name)

			details_obj.profile_pic.save(image_name, image_data, save=True)

			return HttpResponse("Profile picture saved.")

		except Exception, e:
			return HttpResponseBadRequest("An expcetion was caught: Profile Picture not saved.", e)

	def get_profile_pic(self, request):

		json_data = json.loads(request.body)

		user = CustomUser.objects.get(email=json.data.get("email"))
		user_type = json_data.get("user_type")

		if user_type == "D":
			details_obj = DriverDetails.objects.get(user_instance=user)
		elif user_type == "C":
			details_obj = CustomerDetails.objects.get(user_instance=user)
		else:
			details_obj = None
		try:
			image_data = ContentFile(b64encode(details_obj.profile_pic.file.read()))
			image_dict = json.dumps({"b64_img" : image_data})
			return JsonResponse(image_dict)
		except Exception as e:
			return HttpResponseBadRequest("Something went wrong when fetching Profile Picture.")


	def get_driver_details(self, request):

		"""
			Rewrite to use request.user?

		"""

		try:

			driver_email = request.session['trip_driver_email']

			user_instance = CustomUser.objects.get(email=driver_email)

			dd = DriverDetails.objects.get(user_instance=user_instance)
			return HttpResponse(serializers.serialize("json", [user_instance, dd]))
		except Exception, e:
			return HttpResponse("Driver not found")

		return HttpResponse("Driver not found")
	def available(self, request):

		user_instance = CustomUser.objects.get(email=request.GET['email'])

		dd = DriverDetails.objects.get(user_instance=user_instance)

		return dd.available

	def post(self, request):
		if request.path == '/get_driver_details':
			return self.get_driver_details(request)
		elif request.path =='/add_profile_pic':
			if request.user.user_type == 'C':
				return self.add_profile_pic(request, CustomerDetails.objects.get(user_instance=request.user))
			elif request.user.user_type == 'D':
				return self.add_profile_pic(request, DriverDetails.objects.get(user_instance=request.user))
			else:
				return HttpResponseBadRequest("Invalid user type")
		elif request.path =='/get_profile_pic':
			return self.get_profile_pic(request)

		return HttpResponseBadRequest("Bad url")

	def get(self, request):
		if request.path == '/available/':
			return HttpResponse(self.available(request))
		return HttpResponseBadRequest("Bad URL")

class CustomerAlreadyExistsException(Exception):

	pass
