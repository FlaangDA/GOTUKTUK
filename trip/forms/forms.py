from django.forms import ModelForm
from trip.models import TripSession, TripRequest

class CreationFormTripRequest(ModelForm):
	class Meta:
		model = TripRequest
		fields = ['pickuplng', 'pickuplat', 'dropofflng', 'dropofflat', 'requestedprice', 'acceptedprice']
		
class CreationFormTripSession(ModelForm):
	class Meta:
		model = TripSession
		fields = '__all__'
