from django.contrib import admin
from models import DebtTable
from users.models import DriverDetails
# Register your models here.

class DriverDetailsInline(admin.TabularInline):
	model = DriverDetails


class DebtTableAdmin(admin.ModelAdmin):
	model = DebtTable
	#inlines = [DriverDetailsInline, ]

	list_display = ['driver_name', 'driver_email','debt', ]

	readonly_fields = ('driver_name', 'driver_email',)

	exclude = ('driver',)

	def has_add_permission(self, request):
	    num_objects = self.model.objects.count()
	    if num_objects >= 1:
	      return False
	    else:
	      return True

	def has_delete_permission(self, request, obj=None):
	    num_objects = self.model.objects.count()
	    if num_objects >= 1:
	      return False
	    else:
	      return True

admin.site.register(DebtTable, DebtTableAdmin)