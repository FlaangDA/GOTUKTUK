from django.forms import ModelForm
from packagedeals.models import PackageDeal

class CreationFormPackageDeal(ModelForm):

	class Meta:
		model = PackageDeal
		fields = '__all__'