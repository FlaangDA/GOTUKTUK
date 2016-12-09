from rest_framework import serializers
from models import CustomUser, CustomerDetails, DriverDetails


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = '__all__'

	errors = {
        'email': {'required': True},
        'firstname': {'required': True},
        'lastname': {'required': True},
    } 


class CustomerDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomerDetails
		fields = '__all__'