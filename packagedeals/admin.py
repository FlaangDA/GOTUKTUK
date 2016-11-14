from django.contrib import admin
from django import forms
from models import PackageDeal
from destinations.models import Destination, Visit

# Register your models here.

class DestinationInline(admin.TabularInline):
	model = Destination

	can_delete = False

	raw_id_fields = ('packagedeal', )


class PackageDealChangeForm(forms.ModelForm):

	class Meta:
		model = PackageDeal
		fields = ('name', 'header_image', 'description', 'price', 'time_first_from', 'time_first_to', 'time_second_from', 'time_second_to', 'pickuppoint', 'dropoffpoint')

class PackageDealAdmin(admin.ModelAdmin):
	form = PackageDealChangeForm
	inlines = [DestinationInline, ]
	readonly_fields =  ['image_tag',]

	list_display = ('name', 'description', 'price')

admin.site.register(PackageDeal, PackageDealAdmin)
