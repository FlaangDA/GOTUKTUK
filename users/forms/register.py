from django import forms
from users.models import CustomUser, DriverDetails, CustomerDetails
from debtcollector.models import DebtTable

class RegistrationFormCustomer(forms.ModelForm):

	email = forms.EmailField(widget=forms.TextInput,label="Email")
	password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput, label="Password (again)")

	class Meta:
		model = CustomUser
		related_name = "gtt_customer"
		fields = ['email', 'dob', 'firstname', 'lastname']

		widgets = {
			'password1' : forms.PasswordInput(),
			'password2' : forms.PasswordInput(),
		}

	def clean_password(self):

		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 in self.cleaned_data['password1'] and password2 in self.cleaned_data['password2']:
			if password1 != password2:
				raise forms.ValidationError("Passwords don't match.")

		return self.cleaned_data

	def save(self, commit=True):
		
		user = super(RegistrationFormCustomer, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		user.user_type='C'
		user.is_admin = False
		user.is_staff = False
		user.is_superuser = False

		if commit:
			user.save()
		return user

	def clean_username(self, username):
		user_model = CustomUser

		try:
			user_model.objects.get(email=username)
		except user_model.DoesNotExist:
			return username
		raise forms.ValidationError(_("This username already exists"))

class RegistrationFormCustomerDetails(forms.ModelForm):

	class Meta:
		model = CustomerDetails
		related_name = "customer_details"
		fields = ['phone', 'facebookurl', 'nationality']

	def save(self, commit=True):
		details = super(RegistrationFormCustomerDetails, self).save(commit=False)

		if commit:
			details.save()

		return details

class RegistrationFormDriver(forms.ModelForm):

	email = forms.EmailField(widget=forms.TextInput,label="Email")
	password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput, label="Password (again)")

	class Meta:
		model = CustomUser
		related_name = "gtt_driver"
		fields = ['email', 'dob', 'firstname', 'lastname']

		widgets = {
			'password1' : forms.PasswordInput(),
			'password2' : forms.PasswordInput(),
		}

	def clean_password(self):

		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 in self.cleaned_data['password1'] and password2 in self.cleaned_data['password2']:
			if password1 != password2:
				raise forms.ValidationError("Passwords don't match.")

		return self.cleaned_data

	def save(self, commit=True):

		user = super(RegistrationFormDriver, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		user.user_type = 'D'
		if commit:
			user.save()
		return user

	def clean_username(self, username):
		user_model = CustomUser

		try:
			user_model.objects.get(email=username)
		except user_model.DoesNotExist:
			return username
		raise forms.ValidationError(_("This username already exists"))

class RegistrationFormDriverDetails(forms.ModelForm):

	class Meta:
		model = DriverDetails
		related_name = "driver_details"
		fields = ['phone', 'facebookurl']

	def save(self, commit=True):
		details = super(RegistrationFormDriverDetails, self).save(commit=False)
		if commit:
			details.save()
		print "JHESUS CHRIST", details.user_instance
		user = details.user_instance
		print user.firstname, user.lastname
		driver_name = user.firstname + " " + user.lastname
		debt = DebtTable(driver = details, debt = 0.0, driver_email=user.email, driver_name=driver_name)
		
		debt.save()
		print debt
		return details





