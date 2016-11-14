from src import settings

from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model as user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.forms import ModelForm, PasswordInput
from models import CustomUser, CustomerDetails, DriverDetails, GoTukTukAdminDetails
from forms.register import RegistrationFormCustomer, RegistrationFormCustomerDetails
from forms.forms import CustomerDetailsChangeForm

import logging
l = logging.getLogger('django.request')
l2 = logging.getLogger('default')
from django.utils.encoding import force_text

class CustomerInline(admin.StackedInline):
	model = CustomerDetails

	form = CustomerDetailsChangeForm

	readonly_fields =  ['image_tag',]
	
class DriverInline(admin.StackedInline):
	model = DriverDetails

	fk_name = 'user_instance'

	exclude = ('lon', 'lat', 'hasTripRequest', 'available',)

	verbose_name_plural = "Driver Details"

	fields = ('image_tag', )

	readonly_fields = ['image_tag']


class GoTukTukAdminCreationForm(forms.ModelForm):
	"""A form for creating new admins. Includes all the required fields, plus a repeated password."""
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

	class Meta:
		model = CustomUser
		fields = ('email', 'firstname', 'lastname', 'password1', 'password2', 'dob', 'date_joined', 'user_type', 'is_admin', 'is_active')


	def is_valid(self):
		logging.info(force_text(self.errors))
		return super(GoTukTukAdminCreationForm, self).is_valid()

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match.")

		return password2

	def save(self, commit=True):
		user = super(GoTukTukAdminCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])

		if commit:
			user.save()
		return user

class GoTukTukAdminChangeForm(forms.ModelForm):

	password = ReadOnlyPasswordHashField(label = ("Password"), help_text= ("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"../password/\">this form</a>."))

	class Meta:
		model = CustomUser
		fields = ('email', 'password', 'firstname', 'lastname',)

		widgets = {
			'password' : forms.PasswordInput(),
		}

	def clean_password(self):
		return self.initial["password"]

class UserAdmin(BaseUserAdmin):
	form = GoTukTukAdminChangeForm
	add_form = GoTukTukAdminCreationForm
	inlines = [DriverInline]
	readonly_fields = ['user_type', 'is_active', 'is_admin']
	# The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
	list_display = ('email', 'firstname', 'lastname', 'is_admin', 'user_type', 'is_active')
	list_filter = ('is_admin',)
	fieldsets = (
		(None, {'fields': ('email', 'password',)}),
		('Personal info', {'fields': ('firstname', 'lastname',)}),
		('Permissions', {'fields': ('is_admin', 'password',)}),
		)
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
	add_fieldsets = ((None, {'classes': ('wide',),'fields': ('email', 'firstname', 'lastname', 'password', 'dob', 'date_joined', 'user_type', 'is_active',)}),)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

class ExtendedUserAdmin(UserAdmin):
	inlines = UserAdmin.inlines + [DriverInline]
"""

Do I need to create a DriverAdmin and CustomerAdmin, and then pass inlines = [DriverAdminInline, DriverDetailsInline] for drivers and similar for customer?

"""
admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
