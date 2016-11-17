from __future__ import unicode_literals

from django.db import models
from users.models import DriverDetails

class DebtTable(models.Model):

	driver = models.OneToOneField(DriverDetails, blank = True, null= True)
	debt = models.FloatField(default=0.0)

	driver_name = models.CharField(max_length=100, default="")
	driver_email = models.CharField(max_length=100, default="")

	class Meta:
		verbose_name = "Debt"

# Create your models here.
