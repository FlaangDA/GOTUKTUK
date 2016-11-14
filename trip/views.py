import json, simplejson
from base64 import b64decode, b64encode

# Django packages
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.http import HttpResponse, JsonResponse, Http404
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.core.files.base import ContentFile

# Apps
from users.models import CustomUser, CustomerDetails, DriverDetails
from users.views import DetailsView
from models import TripRequest, TripSession
from forms import CreationFormTripRequest, CreationFormTripSession
from fields import TripRequestSerializer
from pricing.views import calculate_price
from datetime import datetime

import logging
l2 = logging.getLogger('default')
# Create your views here.

class TripView(View):

	#get Daniel's admin object here so we can let him know how much money he is owed.

	def add_rating(self, request):

		dict_data = json.loads(request.body)

		tripsession = TripSession.objects.get(id=request.session['tripsessionID'])

		if request.POST['feedback']:
			tripsession.feedback = request.POST['feedback']

		if request.POST['rating']:
			tripsession.rating = request.POST['rating']

		tripsession.save()

		return HttpResponse("Rating saved.")

	def finish_trip(self, request):
		request.session['triprequest_tripcomplete'] = True
		request.session['trip_active'] = False

		triprequest = TripRequest.objects.get(id=request.session['triprequestID'])
		tripsession = TripSession.objects.get(triprequest=triprequest)

		triprequest.tripcompleted = True
		tripsession.tripcomplete = True

		conv_time = str(tripsession.triporderdatetime)[:19]
		str_datetime = datetime.strptime(conv_time, '%Y-%m-%d %H:%M:%S').time()

		income_dict = calculate_price(str_datetime, int(tripsession.etakm))

		tripsession.customer_pays = income_dict.get("customer_paid")
		tripsession.profit = income_dict.get("driver_owes")
		DriverDetails.objects.get(user_instance=triprequest.driver).debtUSD += income_dict.get("driver_owes")

		triprequest.save()
		tripsession.save()

		return HttpResponse("Trip finished.")

	def accept_triprequest(self, request):


		dict_data = json.loads(request.body)
		
		triprequest = TripRequest.objects.get(id=dict_data.get('tripreqID'))
		request.session['triprequestID'] = triprequest.id

		if triprequest is not None and not triprequest.is_active() and triprequest.tripcompleted is False:
			triprequest.active = True
			triprequest.driver = CustomUser.objects.get(email=dict_data.get('driver'))
			request.session['triprequest_tripcomplete'] = False
			request.session['trip_active'] = True
			triprequest.accepted = True
			triprequest.save()
			trobj = TripSession.objects.create_tripsession(triprequest, dict_data)
			request.session['tripsessionID'] = trobj.id
			return HttpResponse(serializers.serialize("json", [trobj,]), "Triprequest successfully accepted, created new Tripsession")
		else:
			return HttpResponse("TripRequest has already been accepted by someone else.")

	def check_triprequest(self, request):

		#What happens when a triprequest takes too long to complete? What if the customer orders another trip without finishing this one?

		#Creating function delete_triprequest.

		#dict_data = json.loads(request.body)

		#l2.debug(dict_data)
		#l2.debug(dict_data.get('triprequestID'))
		l2.debug(request.user)
		l2.debug(request.user.is_authenticated())
		try:
			triprequest = TripRequest.objects.get(id=request.session['triprequestID'])
			if triprequest.accepted:
				return HttpResponse(serializers.serialize("json", [TripSession.objects.get(triprequest=triprequest),])) 

		except Exception, e:	
			l2.error("check_triprequest encountered an exception.", e)
			return HttpResponse("TripRequest not yet accepted.")
		return HttpResponse("TripRequest not yet accepted.")

	def delete_triprequest(self, request=None, triprequestID=None):

		if request:
			json_data = json.loads(request.body)

			obj = TripRequest.objects.get(json_data.get('triprequestID'))

			obj.delete()

		if triprequestID:

			obj = TripRequest.objects.get(id=triprequestID)

			obj.delete()

		return HttpResponse("TripRequest object succesfully deleted")

	def ping_triprequest(self, request):
		
		#Consider implementing a cache-solution, and just update the cache once a driver has a triprequest
		try:

			json_data = json.loads(request.body)

			user_instance = request.user

			dd = DriverDetails.objects.get(user_instance=user_instance)

			dd.lon = json_data.get('lon')
			dd.lat = json_data.get('lat')

			dd.save()

		except Exception, e:
			l2.error(request, user_instance)
		return HttpResponse(serializers.serialize('json', TripRequest.objects.all().filter(tripcompleted=False)), content_type="application/json")

	def setTripRequest(self, user, hasrequest):

		driver = DriverDetails.objects.get(user_instance=user)
		driver.hasTripRequest = hasrequest

		driver.save()

	def check_price(self, request):
		json_data = json.loads(request.body)

		income_dict = calculate_price(datetime.today().time(), int(json_data.get('etakm')))

		return HttpResponse(income_dict.get('customer_paid'))

	def request_trip(self, request):

		json_data = json.loads(request.body)

		requestingCustomer = CustomUser.objects.get(email=json_data.get('customer'))

		if requestingCustomer.is_authenticated():
			form = CreationFormTripRequest(json_data)
			if form.is_valid():
				triprequest = TripRequest.objects.create_triprequest(
					requestingCustomer,
					pickuplat = json_data['pickuplat'],
					pickuplng = json_data['pickuplng'],
					dropofflat = json_data['dropofflat'],
					dropofflng = json_data['dropofflng'],
					requestedprice=json_data['requestedprice'], 
					acceptedprice=json_data['acceptedprice'], 
					active=True)
				#request.session['triprequestID'] = triprequest
				#self.setTripRequest(requestedDriver, True)
				#triprequest.active = True
				triprequest.save()
				request.session['triprequestID'] = triprequest.id
				return HttpResponse(json.dumps(["triprequest id", str(triprequest.id)]), content_type="application/json")
			else:
				return HttpResponse("TripRequest not submitted. Form invalid.")	
		return HttpResponse("TripRequest not submitted. Customer not authenticated.")
		#request_trip should not return a response until a driver has been assigned to

	def get_trip_graphics(self, request):

		"""
		Get the user object.
		Get all tripsession objects connected to this user object(can be filtered)
		For each tripsession object associated with the user, get all TripGraphics objects
		Serialize TripGraphic objects, return them to client.

			{
				"tripsessionID" : {
					"tripGraphics" : {
						"img" : file
					}
				}

			}

		"""

		user = request.user
		if request.user.user_type == 'C':
			triprequests = TripRequest.objects.filter(customer=request.user)
		elif request.user.user_type == 'D':
			triprequests = TripRequest.objects.filter(driver=request.user)
		else:
			triprequests = TripRequest.objects.filter(customer=request.user)

		history_dict = dict()

		for req in triprequests:
			tripsession = TripSession.objects.get(triprequest=req)
			tripgraphic = tripsession.tripsessiongraphic
			image_data = ContentFile(b64encode(tripgraphic.file.read()))
			history_dict[tripsession.id] = image_data

		return JsonResponse(history_dict)

	def getTripData(self, request):
		return None

	def post(self, request, *args, **kwargs):
		if request.path == '/ping_triprequest/':
			return self.ping_triprequest(request)
		elif request.path == '/request_trip/':
			return self.request_trip(request)
		elif request.path == '/accept_triprequest/':
			return self.accept_triprequest(request)
		elif request.path == '/finish_trip/':
			return self.finish_trip(request)
		elif request.path == '/add_rating/':
			return self.add_rating(request)
		elif request.path == '/check_price':
			return self.check_price(request)

		return HttpResponse(status=404)

	def get(self, request):
		if request.path == '/check_triprequest/':
			return self.check_triprequest(request)
		elif request.path == '/get_trip_graphics':
			return self.get_trip_graphics(request)
		return HttpResponse(status=404)


