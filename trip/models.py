from django import forms
from django.db import models
from django.utils import timezone as timezone
from datetime import datetime
import json
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import django
from users.models import CustomUser
from src import settings

# Create your models here.

json.JSONEncoder.default = lambda self,obj: (obj.isoformat() if isinstance(obj, datetime) else None)
"""
models.Manager:

TripManage, TripSessionManager, FareManager

"""

	
class TripSessionManager(models.Manager):
	
	def create_tripsession(self, triprequest, kwargs):
		#remember to call create_tripsession with all arguments for **kwargs "2016-01-12 14:59:49"

		tripsession = self.model(
			triprequest=triprequest,
			pickuplat = kwargs.get('pickuplat'),
			pickuplng = kwargs.get('pickuplng'),
			dropofflat = kwargs.get('dropofflat'),
			dropofflng = kwargs.get('dropofflng'),
			timeconsumed = datetime.strptime(kwargs.get('timeconsumed'), '%H:%M:%S').time(),
			datetimetrip = datetime.strptime(kwargs.get('datetimetrip'), '%Y-%m-%d %H:%M:%S'),
			triporderdatetime = datetime.strptime(kwargs.get('triporderdatetime'), '%Y-%m-%d %H:%M:%S'),
			tripstartdatetime = datetime.strptime(kwargs.get('tripstartdatetime'), '%Y-%m-%d %H:%M:%S'),
			etaarrival = datetime.strptime(kwargs.get('etaarrival'), '%H:%M:%S').time(),
			etatrip = datetime.strptime(kwargs.get('etatrip'), '%H:%M:%S').time(),
			etakm = kwargs.get('etakm'),
			feedback = kwargs.get('feedback'),
			rating = kwargs.get('rating'),
			customer_pays = kwargs.get('customer_pays'),
			)

		tripsession.save(using=self._db)
		return tripsession

	#Here I can create methods that allow me to filter tripsessions by different parameters(e.g distance, price, etc)


class TripRequestManager(models.Manager):
	"""
	def get_queryset(self):
		qs = super(TripRequestManager, self).get_queryset()
		return qs.select_related('driver', 'customer').prefetch_related()
	"""
	def create_triprequest(self, requestingCustomer, **kwargs):

		triprequest = self.model(
			customer = requestingCustomer,
			pickuplat = kwargs.get('pickuplat'),
			pickuplng = kwargs.get('pickuplng'),
			dropofflat = kwargs.get('dropofflat'),
			dropofflng = kwargs.get('dropofflng'),
			requestedprice = kwargs.get('requestedprice'),
			acceptedprice = kwargs.get('acceptedprice'),
			)

		triprequest.save(using=self._db)
		return triprequest


class TripRequest(models.Model):


	customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="gtt_customer_triprequest")
	driver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="gtt_driver_triprequest", blank=True, null=True)

	pickuplng = models.DecimalField(max_digits=9, decimal_places=6, default=11.1111)
	pickuplat = models.DecimalField(max_digits=9, decimal_places=6, default=11.1111)
	dropofflng = models.DecimalField(max_digits=9, decimal_places=6, default=11.1111)
	dropofflat = models.DecimalField(max_digits=9, decimal_places=6, default=11.1111)

	requestedprice = models.FloatField(default=0.0)
	acceptedprice = models.BooleanField(default=False)

	active = models.BooleanField(default=False)
	accepted = models.BooleanField(default=False)

	tripcompleted = models.BooleanField(default=False)

	objects = TripRequestManager()


	class Meta:
		verbose_name = "TripRequest"
		verbose_name_plural = "TripRequests"

	def is_active(self):
		return self.active

	def content(self):
		return {
			"customer" : self.customer.email, 
			"driver" : self.driver.email, 
			"pickuplng" : self.pickuplng, 
			"pickuplat" : self.pickuplat, 
			"dropofflng" : self.dropofflng, 
			"dropofflat" : self.dropofflat, 
			"requestedprice" : str(self.requestedprice), 
			"acceptedprice" : str(self.acceptedprice), 
			"active" : str(self.active)
		}

	def natural_key(self):
		return self.id + self.customer.get_by_natural_key(self.customer.email) + self.driver.get_by_natural_key(self.driver.email)

	natural_key.dependencies = ['users.CustomUser']


class TripSession(models.Model):

	"""
	The TripSession.

		- Establishes a foreign key with a Triprequest
		- pickUpPoint are the coordinates for the desired pick-up point
		- dropOffPoint are the coordinates for the desired drop-off point
		- dateTimeTrip is the time of which the trip is ordered
		- timeConsumed is the actual amount of time the trip consumed. Calculated when Trip is ended
		- tripOrderDateTime is the date and time of which the trip was ordered
		- tripStartDateTime is the date and time of which the trip was started
		- etaArrival is the estimated time the driver needs to approach the customer. 
		- etaTrip is the estimated time the trip consumes, and is used to calculate Fare.
		- feedbackDriver is the feedback a driver receives after trip is ended
		- feedbackCustomer is the feedback a customer receives after trip is ended
		- ratingDriver is the rating a driver receives after trip is ended
		- ratingCustomer is the rating a customer receives after trip is ended
	"""

	triprequest = models.ForeignKey(TripRequest, blank = True, null = True)

	pickuplng = models.DecimalField(max_digits=9, decimal_places=6, default=11.1111)
	pickuplat = models.DecimalField(max_digits=9, decimal_places=6, default=11.1111)
	dropofflng = models.DecimalField(max_digits=9, decimal_places=6, default=11.1111)
	dropofflat = models.DecimalField(max_digits=9, decimal_places=6, default=11.1111)

	datetimetrip = models.DateTimeField(default=django.utils.timezone.now)
	timeconsumed = models.TimeField()

	triporderdatetime = models.DateTimeField(default=django.utils.timezone.now)
	tripstartdatetime = models.DateTimeField(default=django.utils.timezone.now)
	tripenddatetime = models.DateTimeField(default=django.utils.timezone.now)

	#remove fields:
	etaarrival = models.TimeField()
	etatrip = models.TimeField()

	#The rounded amount of kilometers of this trip.
	etakm = models.FloatField(default=0.0)

	customer_pays = models.FloatField(default=0.0)
	profit = models.FloatField(default=0.0)

	feedback = models.TextField(max_length=1000)
	rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])

	tripcomplete = models.BooleanField(default=False)

	tripsessiongraphic = models.ImageField(upload_to="tripsession/", default="tripsession/default.jpg")

	objects = TripSessionManager()

	class Meta:
		verbose_name = "Tripsession"
		verbose_name_plural = "Tripsessions"

	def __str__(self):
		return str(self.id)

	def image_tag(self):
		return safestring.mark_safe('<img src="%s" width="150" height="150" />' % (self.tripsessiongraphic.url))

		image_tag.short_description = 'Profile Picture'

class TripGraphics(models.Model):

	tripsession = models.OneToOneField(TripSession, primary_key=True)

	tripgraphic = models.ImageField(upload_to="TripSessionGraphics/", null=True)

	class Meta:
		verbose_name = "TripGraphic"
		verbose_name_plural = "TripGraphics"

	#USDperKm, USDbase are variables set by the system admin. 
	#USDtotal is calculated from etaTrip, etaKM, USDperKm and USDbase

#Include a class FareTable(models.Model) which contains prices for given time specifications.

#Handling it in the views would give me the following pros and cons:
#Pros: Wouldn't have to create multiple models to represent the different time specifications. 
#Cons: Less control over the pricing. Would not be able to adjust the pricing as easily. If I can wrap a logic around the Fare system, using it would be a lot easier.