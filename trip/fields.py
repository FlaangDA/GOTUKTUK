from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from models import TripRequest
from users.fields import CustomUserSerializer, CustomerDetailsSerializer, DriverDetailsSerializer
from users.models import CustomUser

class TripRequestSerializer(serializers.ModelSerializer):

	customer = CustomUserSerializer(source='gtt_customer', validators=[UniqueValidator(queryset=CustomUser.customer_objects)])
	driver = CustomUserSerializer(source='gtt_driver', validators=[UniqueValidator(queryset=CustomUser.driver_objects)])

	class Meta:
		model = TripRequest
		fields = ('customer', 'driver', 'pickuplng', 'pickuplat', 'dropofflng', 'dropofflat', 'requestedprice', 'acceptedprice', 'active')
