from rest_framework import serializers
from models import CustomUser, CustomerDetails, DriverDetails

class CustomUserSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomUser
		fields = ('firstname', 'lastname', 'dob')

class DriverDetailsSerializer(serializers.ModelSerializer):

	class Meta:
		model = DriverDetails
		fields = '__all__'

class CustomerDetailsSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomerDetails
		fields = '__all__'