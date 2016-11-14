from __future__ import unicode_literals

from django.db import models
from packagedeals.models import PackageDeal
from users.models import CustomUser
from django.utils import timezone as timezone

# Create your models here.


class DestinationManager(models.Manager):

	def create_destination(self, lon, lat, name, packagedeal, dest_img, phone_number):

		destination = self.model(
			lon = lon, 
			lat = lat, 
			name = name, 
			packagedeal = packagedeal, 
			destination_image = dest_img,
			phone_number = phone_number)

		destination.save(using=self._db)

		return destination

class VisitManager(models.Manager):

	def create_visit(self, customer, destination):

		visit = self.model(customer = customer, destination = destination)

		visit.save(using=self._db)

		return visit

class Destination(models.Model):
	type_choices = (
	('RST', 'Restaurant'),
	('B', 'Bar'),
	('CL', 'Club'),
	('CA', 'Cafe'),
	('CI', 'Cinema'),
	)

	packagedeal = models.ForeignKey(PackageDeal, blank = True, null = True, default = "")



	destination_image = models.ImageField(upload_to='destinations/hotspots', default='destinations/hotspots/pin_location.png')
	name = models.CharField(max_length=150, default='destination_name', unique=True)
	address = models.CharField(max_length=150, default='default')
	phone_number = models.CharField(max_length=16 ,blank=True) # validators should be a list
	lon = models.CharField(max_length=10, default='0000.00000')
	lat = models.CharField(max_length=10, default='0000.00000')


	objects = DestinationManager()

	class Meta:
		verbose_name = "Hotspot"
		verbose_name_plural = "Hotspots"


	def __str__(self):
		return self.name

class Visit(models.Model):

	customer = models.ForeignKey(CustomUser)

	destination = models.ForeignKey(Destination)

	visited = models.DateTimeField(default=timezone.now)

	objects = VisitManager()


	class Meta:
		verbose_name = "Visit"
		verbose_name_plural = "Visits"

	def __str__(self):
		return '%s %s %s' % (self.customer.firstname, self.customer.lastname, self.destination.name) 