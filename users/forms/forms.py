from django.forms import ModelForm, ModelChoiceField
from users.models import CustomUser, DriverDetails, CustomerDetails

class CustomerDetailsChangeForm(ModelForm):

	class Meta:
		model = CustomerDetails
		#Should not be able to change all fields. None? Or every field except email?
		fields = '__all__'
		
class DriverDetailsChangeForm(ModelForm):

	class Meta:
		model = DriverDetails
		fields = '__all__'
