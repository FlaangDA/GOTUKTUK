from django.forms import ModelForm
from destinations.models import Destination

class CreationFormDestination(ModelForm):

	class Meta:
		model = Destination
		fields = '__all__'