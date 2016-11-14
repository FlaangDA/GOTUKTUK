from django.contrib import admin
from django import forms
from models import Destination, Visit
from packagedeals.models import PackageDeal
# Register your models here.


class VisitAdmin(admin.ModelAdmin):


	list_display = ('customer', 'destination', 'visited')


class DestinationChangeForm(forms.ModelForm):

	class Meta:
		model = Destination
		fields = ('name', 'destination_image', 'phone_number','packagedeal', 'lon', 'lat')

class DestinationAdmin(admin.ModelAdmin):
	form = DestinationChangeForm

	list_display = ('name',)

"""
class VisitAdmin(admin.ModelAdmin):
	inlines = [
		DestinationInline,
	]
"""

admin.site.register(Destination, DestinationAdmin)
admin.site.register(Visit, VisitAdmin)