from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, User, AbstractUser, PermissionsMixin
from django.conf import settings
from django.contrib.auth import get_user_model as user_model

from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.utils import safestring

# Create your models here.

class CustomUserManager(BaseUserManager):

	def create_user(self, email, dob, firstname, lastname, user_type, password=None):
		if not email:
			raise ValueError('Customer must have email address.')
		if not dob:
			raise ValueError('Customer must have valid date of birth.')
		if not (firstname or lastname):
			raise ValueError('Customer must have firstname and lastname')
		if not (user_type == 'C' or 'D'):
			raise ValueError('Only drivers and customers can be created using this method.')


		user = self.model(email=self.normalize_email(email), dob=dob, firstname=firstname, lastname=lastname, user_type = user_type)
		user.set_password(password)
		user.is_admin = False
		user.is_staff = False
		user.is_superuser = False
		user.save(using=self._db)
		#The user is returned from this function. Pass the user as an argument to UserDetailsCreation function.
		return user

	def create_superuser(self, email, dob, firstname, lastname, password=None):


		if not email:
			raise ValueError('Customer must have email address.')
		if not dob:
			raise ValueError('Customer must have valid date of birth.')
		if not (firstname or lastname):
			raise ValueError('Customer must have firstname and lastname')

		user = self.model(email=self.normalize_email(email), dob=dob, firstname=firstname, lastname=lastname)

		user.set_password(password)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.user_type = 'SU'
		user.save(using=self._db)
		
		return user

class CustomerDetailsManager(models.Manager):

	def create_customer_details(self, user, phone, facebookurl, nationality):
		if not user:
			raise ValueError('User is None upon creation. Check if the user was properly created!')
		if not phone:
			raise ValueError('The customer needs to provide a phone number')
		if not facebookurl:
			facebookurl = 'Unknown facebookurl'
		if not nationality:
			nationality = 'Unknown nationality'

		details = self.model(user_instance=user, phone=phone, facebookurl=facebookurl, nationality=nationality)

		details.save(using=self._db)
		return details

class DriverDetailsManager(models.Manager):

	def create_driver_details(self, user, phone, facebookurl):
		if not user:
			raise ValueError('User is None upon creation. Check if the user was properly created!')
		if not phone:
			raise ValueError('The customer needs to provide a phone number')
		if not facebookurl:
			facebookurl = 'Unknown facebookurl'

		details = self.model(user_instance=user, phone=phone, facebookurl=facebookurl)

		details.save(using=self._db)
		return details


class GoTukTukAdminManager(models.Manager):

	def create_admin_details(self, user):
		if not user:
			raise ValueError('User is None upon creation. Check if the user was properly created!')

		details = self.model(user_instance=user)
		details.is_admin = True
		details.user_type = 'SU'

		details.save(using=self._db)

		return details


class CustomersManager(models.Manager):
	def get_queryset(self):
		return super(CustomersManager, self).get_queryset().filter(user_type='C')

class DriversManager(models.Manager):
	def get_queryset(self):
		return super(DriversManager, self).get_queryset().filter(user_type='D')

class CustomUser(AbstractBaseUser, PermissionsMixin):
	type_choices = (
		('SU', 'Superuser'),
		('C', 'Customer'),
		('D', 'Driver'),
		)

	user_type = models.CharField(max_length=2, choices=type_choices, default='D')

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['firstname', 'lastname', 'dob']
	UNIQUE_TOGETHER = ('email', )


	email = models.EmailField(verbose_name="email address",  max_length=255, unique=True)
	lastname = models.CharField(max_length=40)
	firstname = models.CharField(max_length=40)
	dob = models.DateField()
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=timezone.now)


	objects = CustomUserManager()
	customer_objects = CustomersManager()
	driver_objects = DriversManager()

	def __init__(self, *args, **kwargs):
	        super(CustomUser, self).__init__(*args, **kwargs)
	        passwd = [field for field in self._meta.fields if field.attname is 'password']
	        if passwd:
	            passwd[0].blank = True

	class Meta:
		db_table = 'users_customuser'
		managed = True

	def get_user_type(self):
		return self.user_type

	def __str__(self):
		return '%s %s' % (self.firstname, self.lastname)

	def get_id_by_email(self):
		return self.email

	def is_staff(self):
		return self.is_admin

	def get_short_name(self):
		return self.firstname

	def get_full_name(self):
		return ''.join(self.lastname, " ", self.firstname)

	def get_is_active(self):
		return self.is_active

	def natural_key(self):
		return (self.lastname, self.firstname)

class CustomerDetails(models.Model):
	user_instance = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="gtt_customer")

	phone = models.CharField(max_length=25)
	facebookurl = models.URLField(blank=True)
	nationality = models.CharField(max_length=50, blank=True)

	profile_pic = models.ImageField(upload_to="profilepics/", default="profilepics/default.png")

	objects = CustomerDetailsManager()

	class Meta:
		verbose_name = "Customer"
		verbose_name_plural = "Customers"
		db_table = 'users_customerdetails'


	def get_phone(self):
		return self.phone

	def get_facebookUrl(self):
		return self.facebookurl

	def get_nationality(self):
		return self.nationality

	def image_tag(self):
		return safestring.mark_safe('<img src="%s" width="150" height="150" />' % (self.image_tag.url))

	image_tag.short_description = 'Profile Picture'

class DriverDetails(models.Model):
	user_instance = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="gtt_driver")

	phone = models.CharField(max_length=25)
	facebookurl = models.URLField(blank=True)
	available = models.BooleanField(default=False)
	lon = models.DecimalField(max_digits=9, decimal_places=6, default=000.00000)
	lat = models.DecimalField(max_digits=9, decimal_places=6, default=000.00000)
	#add trip_request table to Trip app
	#add location as well?

	profile_pic = models.ImageField(upload_to="profilepics/", default="profilepics/default.png")

	debtUSD = models.FloatField(default=0)

	hasTripRequest = models.BooleanField(default=False)

	objects = DriverDetailsManager()

	class Meta:
		verbose_name = "Driver"
		verbose_name_plural = "Drivers"
		db_table = 'users_driverdetails'


	def get_phone(self):
		return self.phone

	def get_facebookUrl(self):
		return self.facebookurl

	def is_available(self):
		return self.available

	def has_triprequest(self):
		return self.hasTripRequest

	def image_tag(self):
		return safestring.mark_safe('<img src="%s" width="150" height="150" />' % (self.profile_pic.url))

	image_tag.short_description = 'Profile Picture'



class GoTukTukAdminDetails(models.Model):
	
	user_instance = models.OneToOneField(settings.AUTH_USER_MODEL)

	class Meta:
		verbose_name = "GoTukTukAdmin"
		verbose_name_plural = "GoTukTukAdmins"
