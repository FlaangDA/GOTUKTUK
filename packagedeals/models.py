from __future__ import unicode_literals

from django.db import models
import django
from django.utils import safestring
# Create your models here.


class PackageDealManager(models.Manager):

	def create_packagedeal(self, kwargs):
		packagedeal = self.model(
			name = kwargs.get('name'),
			header_image = kwargs.get('header_image'),
			description = kwargs.get('description'),
			price = kwargs.get('price'),
			time_first_from = kwargs.get('time_first_from'),
			time_first_to = kwargs.get('time_first_to'),
			time_second_from = kwargs.get('time_second_from'),
			time_second_to = kwargs.get('time_second_to'),
			pickuppoint = kwargs.get('pickuppoint'),
			dropoffpoint = kwargs.get('dropoffpoint')
			)
		packagedeal.save(using=self._db)

		return packagedeal

class PackageDeal(models.Model):

	name = models.CharField(max_length=100, primary_key=True, unique=True)
	header_image = models.ImageField(upload_to='packagedeals/headers', default='packagedeals/headers/hillary.jpg')
	description = models.CharField(max_length=1000, default=' ')
	price = models.FloatField(default=0.0)
	time_first_from = models.DateTimeField(default=django.utils.timezone.now)
	time_first_to = models.DateTimeField(default=django.utils.timezone.now)
	time_second_from = models.DateTimeField(default=django.utils.timezone.now)
	time_second_to = models.DateTimeField(default=django.utils.timezone.now)

	pickuppoint = models.CharField(max_length=15, default='0000.0000')
	dropoffpoint = models.CharField(max_length=15, default='0000.0000')

	objects = PackageDealManager()

	class Meta:
		verbose_name = "Packagedeal"
		verbose_name_plural = "Packagedeals"

	def __str__(self):
		return self.name

	def image_tag(self):
		return safestring.mark_safe('<img src="%s" width="150" height="150" />' % (self.header_image.url))

	image_tag.short_description = 'Header Image'