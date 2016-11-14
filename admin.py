from django.contrib import admin
from models import EarlyMorning, Morning, Afternoon, EarlyAfternoon, LateAfternoon, Evening, Nighttime, EarlyMorningProfit, MorningProfit, AfternoonProfit, EarlyAfternoonProfit, LateAfternoonProfit, EveningProfit, NighttimeProfit
from users.models import DriverDetails

# Register your models here.





class EarlyMorningAdminInline(admin.TabularInline):
	model = EarlyMorningProfit

class EarlyMorningAdmin(admin.ModelAdmin):
	"""
	The ModelAdmin class for EarlyMorningAdmin.

	All fields can be changed except for the name of the period.

	Only one instance of this model can be added. 
	"""
	inlines = [EarlyMorningAdminInline, ]
	readonly_fields = ('name', )
	list_display = ['name'] + [field.name for field in EarlyMorning._meta.fields if field.name != "id" and field.name != "name"]

	def has_add_permission(self, request):
	    num_objects = self.model.objects.count()
	    if num_objects >= 1:
	      return False
	    else:
	      return True

class MorningAdminInline(admin.TabularInline):
	model = MorningProfit

class MorningAdmin(admin.ModelAdmin):
	"""
	The ModelAdmin class for MorningAdmin.

	All fields can be changed except for the name of the period.

	Only one instance of this model can be added. 
	"""
	inlines = [MorningAdminInline, ]
	readonly_fields = ('name', )
	list_display = ['name'] + [field.name for field in Morning._meta.fields if field.name != "id" and field.name != "name"]

	def has_add_permission(self, request):
	    num_objects = self.model.objects.count()
	    if num_objects >= 1:
	      return False
	    else:
	      return True

class AfternoonAdminInline(admin.TabularInline):
	model = AfternoonProfit

class AfternoonAdmin(admin.ModelAdmin):
	"""
	The ModelAdmin class for AfternoonAdmin.

	All fields can be changed except for the name of the period.

	Only one instance of this model can be added. 
	"""
	inlines = [AfternoonAdminInline, ]
	readonly_fields = ('name', )
	list_display = ['name'] + [field.name for field in Afternoon._meta.fields if field.name != "id" and field.name != "name"]

	def has_add_permission(self, request):
	    num_objects = self.model.objects.count()
	    if num_objects >= 1:
	      return False
	    else:
	      return True

class EarlyAfternoonAdminInline(admin.TabularInline):
	model = EarlyAfternoonProfit

class EarlyAfternoonAdmin(admin.ModelAdmin):
	"""
	The ModelAdmin class for EarlyAfternoonAdmin.

	All fields can be changed except for the name of the period.

	Only one instance of this model can be added. 
	"""
	inlines = [EarlyAfternoonAdminInline, ]
	readonly_fields = ('name', )
	list_display = ['name'] + [field.name for field in EarlyAfternoon._meta.fields if field.name != "id" and field.name != "name"]

	def has_add_permission(self, request):
	    num_objects = self.model.objects.count()
	    if num_objects >= 1:
	      return False
	    else:
	      return True

class LateAfternoonAdminInline(admin.TabularInline):
	model = LateAfternoonProfit

class LateAfternoonAdmin(admin.ModelAdmin):
	"""
	The ModelAdmin class for LateAfternoonAdmin.

	All fields can be changed except for the name of the period.

	Only one instance of this model can be added. 
	"""
	inlines = [LateAfternoonAdminInline, ]
	readonly_fields = ('name', )
	list_display = ['name'] + [field.name for field in LateAfternoon._meta.fields if field.name != "id" and field.name != "name"]

	def has_add_permission(self, request):
	    num_objects = self.model.objects.count()
	    if num_objects >= 1:
	    	return False
	    else:
	    	return True

class EveningAdminInline(admin.TabularInline):
	model = EveningProfit

class EveningAdmin(admin.ModelAdmin):
	"""
	The ModelAdmin class for EveningAdmin.

	All fields can be changed except for the name of the period.

	Only one instance of this model can be added. 
	"""
	inlines = [EveningAdminInline, ]
	readonly_fields = ('name', )
	list_display = ['name'] + [field.name for field in Evening._meta.fields if field.name != "id" and field.name != "name"]

	def has_add_permission(self, request):
	    num_objects = self.model.objects.count()
	    if num_objects >= 1:
	      return False
	    else:
	      return True

class NighttimeAdminInline(admin.TabularInline):
	model = NighttimeProfit

class NighttimeAdmin(admin.ModelAdmin):
	"""
	The ModelAdmin class for NighttimeAdmin.

	All fields can be changed except for the name of the period.

	Only one instance of this model can be added. 
	"""
	inlines = [NighttimeAdminInline, ]
	readonly_fields = ('name', )
	list_display = ['name'] + [field.name for field in Nighttime._meta.fields if field.name != "id" and field.name != "name"]

	def has_add_permission(self, request):
	    num_objects = self.model.objects.count()
	    if num_objects >= 1:
	      return False
	    else:
	      return True

admin.site.register(EarlyMorning, EarlyMorningAdmin)
admin.site.register(Morning, MorningAdmin)
admin.site.register(Afternoon, AfternoonAdmin)
admin.site.register(EarlyAfternoon, EarlyAfternoonAdmin)
admin.site.register(LateAfternoon, LateAfternoonAdmin)
admin.site.register(Evening, EveningAdmin)
admin.site.register(Nighttime, NighttimeAdmin)