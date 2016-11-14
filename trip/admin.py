from django.contrib import admin
from django import forms
from models import TripSession, TripRequest
from users.models import CustomUser, DriverDetails, CustomerDetails
from destinations.models import Destination, Visit
from packagedeals.models import PackageDeal
# Register your models here.


"""
	- A ChangeForm should only be made if the admin is allowed to change any of the data already submitted to the db

"""


class TripSessionInline(admin.StackedInline):

	model = TripSession
	can_delete = False
	
	def has_change_permission(self, request, obj):
		return False

	def has_delete_permission(self, request, obj):
		return False

	def has_module_permission(self, request):
		return True


class TripSessionAdmin(admin.ModelAdmin):

	#inlines = [TripSessionInline, ]

	list_display = ('triprequest', 'pickuplng', 'pickuplat', 'dropofflng', 'dropofflat', 'datetimetrip', 'timeconsumed', 'triporderdatetime','tripstartdatetime','tripenddatetime','etaarrival', 'etatrip', 'etakm', 'feedback', 'rating' , 'tripcomplete')

	readonly_fields = ['image_tag',]

admin.site.register(TripSession, TripSessionAdmin)