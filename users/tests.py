from django.test import TestCase
from django.test import Client
import simplejson, json
# Create your tests here.


class TestCalls(TestCase):

	def test_all(self):


		c = Client()
		c2 = Client()
		c3 = Client()
		c4 = Client()

		#create a user

		json_data = { "lastname" : "Fladbyy", "firstname" : "Torgeir", "email" : "torgeir.fladbyy@gmail.com",  "password1" : "267ec600500",  "password2" : "267ec600500",  "phone" : "95936294", "dob" : "2016-01-17", "nationality" : "Norwegian", "facebookurl" : "facebook.com"}
		
		create_customer = c.post("/create_customer/", json_data)

		#create_customer = c.post("/create_customer/", json_data)

		print create_customer.status_code
		print create_customer.content



		json_data = {"lastname" : "Borthen",
		"firstname" : "Henrik",
		"email" : "henrik.borthen@gmail.com", 
		"password1" : "267ec600500", 
		"password2" : "267ec600500", 
		"phone" : "95936294",
		"dob" : "2016-01-17",
		"nationality" : "Norwegian",
		"facebookurl" : "facebook.com"}
		
		create_customer = c4.post("/create_customer/", json_data)

		print create_customer.status_code
		print create_customer.content


		json_data = {
			"lastname" : "Browne", 
			"firstname" : "Henrik", 
			"email" : "henrik.browne@gmail.com", 
			"dob" : "2016-01-17", 
			"phone" : "98237897", 
			"facebookurl" : "www.facebook.com", 
			"password1" : "267ec600500",
			"password2" : "267ec600500"}

		create_driver = c2.post("/create_driver/", json_data)

		print create_driver.status_code
		print create_driver

		json_data = {
			"lastname" : "Sjoetveit", 
			"firstname" : "Sveinung", 
			"email" : "sveinung.Sjoetveit@gmail.com", 
			"dob" : "2016-01-17", 
			"phone" : "98237897", 
			"facebookurl" : "www.facebook.com", 
			"password1" : "267ec600500", 
			"password2" : "267ec600500"}

		create_driver = c3.post("/create_driver/", json_data)

		print create_driver.status_code
		print create_driver

		#log the user in

		json_data = {"email" : "torgeir.fladbyy@gmail.com", "password" : "267ec600500"}

		login_user = c.post("/login/", json_data)
		print login_user.status_code
		print login_user


		json_data = {"email" : "henrik.borthen@gmail.com", "password" : "267ec600500"}

		login_user = c4.post("/login/", json_data)
		print login_user.status_code
		print login_user


		
		"""
		json_data = {"email" : "torgeir.fladbyy@gmail.com", "password" : "267ec600500"}

		logout = c.post("/logout/", json_data)
		print logout.status_code
		print "Logout status code: ", logout
		"""
		json_data = {"email" : "henrik.browne@gmail.com", "password" : "267ec600500" }

		login_user = c2.post("/login/", json_data)
		print login_user.status_code
		print login_user

		json_data = {"email" : "sveinung.Sjoetveit@gmail.com", "password" : "267ec600500"}

		login_user = c3.post("/login/", json_data)

		print login_user.status_code
		print login_user


		json_data = {"email" : "henrik.browne@gmail.com"}

		disable = c2.post("/disable_driver/", json_data)
		print disable.status_code
		print disable


		json_data = {"email" : "henrik.browne@gmail.com"}

		enable = c2.post("/enable_driver/", json_data)
		print enable.status_code
		print enable

		available_drivers = c.get("/available_drivers/")
		print available_drivers.status_code
		print "available drivers: ", available_drivers.json()

		json_data = {
			"customer" : "torgeir.fladbyy@gmail.com", 
			"driver" : "sveinung.Sjoetveit@gmail.com", 
			"pickuppoint" : "1111.12345", 
			"dropoffpoint" : "1112.12312", 
			"requestedprice" : "4.00", 
			"acceptedprice" : "True"}
		request_trip = c.post("/request_trip/", json_data)

		print request_trip
		print "request trip: ", request_trip.content

		json_data = {"driver" : "sveinung.Sjoetveit@gmail.com"}

		ping_triprequest = c3.get("/ping_triprequest/", json_data)

		
		print ping_triprequest
		print "ping ping_triprequest: ", ping_triprequest.content


		json_data={"customer" : "henrik.browne@gmail.com", "driver" : "sveinung.Sjoetveit@gmail.com", "pickuppoint" : "1111.12345", "dropoffpoint" : "1112.12345", "datetimetrip" : "2016-01-12 14:59:49", "timeconsumed" : "00:00:00", "tripstartdatetime": "2016-01-12 15:00:00", "triporderdatetime" : "2016-01-12 15:00:00", "etaarrival": "15:15:00", "etatrip" : "00:15:00", "etakm" : "5.0", "feedback" : "very good", "rating" : "5", "tripcomplete" : "False"}
		accept_trip = c3.post("/accept_triprequest/", json_data)

		print accept_trip

		"""


		#extract user information

		#json_data = {"email" : "torgeir.fladbyy@gmail.com"}

		#get_user_data = c.post("/action/", json_data)

		json_data = {"lastname" : "Fladbyy","firstname" : "Torgeir","email" : "torgeir.fladbyy@gmail.com", "password" : "267ec600500", "phone" : "95936294","dob" : "2016-01-17","nationality" : "Norwegian","facebookurl" : "facebook.com"}
		
		create_customer = c.post("/user_action/", json_data)

		print create_customer.status_code
		print create_customer

		#I can now get the data I want as long as i specify the action on the server. Next up is creating the relations between trips and users.

		#creating a driver, which I can use to create a Trip.

		#log the driver in
		json_data = {"email" : "henrik.browne@gmail.com", "password" : "321bca"}

		login_user = c.post("/auth/", json_data)

		print "login_driver status_code : ", login_user.status_code
		print "login_driver: " , login_user

		#creating a new trip, based on the email address of a customer and a driver

		json_data = {"customer" : "torgeir.fladbyy@gmail.com", "driver" : "henrik.browne@gmail.com", "pickUpPoint" : "1234asdvsd", "dropOffPoint" : "1234asdvsd", "dateTimeTrip" : "2016-01-23 14:23:21", "timeConsumed" : "05:30:02", "tripOrderDateTime" : "2015-11-11 14:23:21", "tripStartDateTime" : "2015-11-11 14:23:21", "etaArrival" : "09:09:20", "etaTrip" : "07:30:02", "etaKM" : "4", "feedbackDriver" : "very bad", "feedbackCustomer" : "soo shitty", "ratingDriver" : "1", "ratingCustomer" : "2"}
		create_trip = c.post("/new_trip/", json_data)

		print create_trip.status_code
		print create_trip
		show_all = c.post("/show_all/")
		print show_all.status_code
		print show_all
		#get trips between customer and driver

		json_data = {"customer" : "torgeir.fladbyy@gmail.com", "driver" : "henrik.browne@gmail.com"}

		get_trip = c.post("/get_trip/", json_data)
		print get_trip.status_code, ": trip status_code"
		print get_trip

		json_data = {"email" : "torgeir.fladbyy@gmail.com"}

		logout_user = c.post("/logout/", json_data)

		"""


"""

from django.test import Client
import simplejson

c = Client()
c2 = Client()

#create a user

json_data = {"lastname" : "Fladbyy","firstname" : "Torgeir","email" : "torgeir.fladbyy@gmail.com", "password" : "267ec600500", "phone" : "95936294","dob" : "2016-01-17","nationality" : "Norwegian","facebookurl" : "facebook.com"}

create_customer = c.post("/action/", json_data)

print create_customer.status_code

#log the user in

json_data = {"email" : "torgeir.fladbyy@gmail.com", "password" : "267ec600500"}

login_user = c.post("/auth/", json_data)
print login_user.status_code

#extract user information

json_data = {"email" : "torgeir.fladbyy@gmail.com"}

get_user_data = c.post("/action/", json_data)

#I can now get the data I want as long as i specify the action on the server. Next up is creating the relations between trips and users.

#creating a driver, which I can use to create a Trip.

json_data = {"lastname" : "Browne", "firstname" : "Henrik", "email" : "henrik.browne@gmail.com", "dob" : "2016-01-17", "phone" : "98237897", "password" : "321bca"}

create_driver = c2.post("/action/", json_data)

print create_driver.status_code

#creating a new trip, based on the email address of a customer and a driver

json_data = {"customer" : "torgeir.fladbyy@gmail.com", "driver" : "henrik.browne@gmail.com", "pickUpPoint" : "1234asdvsd", "dropOffPoint" : "1234asdvsd", "dateTimeTrip" : "2016-01-23 14:23:21", "timeConsumed" : "05:30:02", "tripOrderDateTime" : "2015-11-11 14:23:21", "tripStartDateTime" : "2015-11-11 14:23:21", "etaArrival" : "09:09:20", "etaTrip" : "07:30:02", "etaKM" : "4", "feedbackDriver" : "very bad", "feedbackCustomer" : "soo shitty", "ratingDriver" : "1", "ratingCustomer" : "2"}
create_trip = c.post("/new_trip/", json_data)

print create_trip.status_code
print create_trip

#show all users

show_all = c.post("/show_all/")
print show_all.status_code
print show_all

#get trips between customer and driver

json_data = {"customer" : "torgeir.fladbyy@gmail.com", "driver" : "henrik.browne@gmail.com"}

get_trip = c.post("/get_trip/", json_data)
print get_trip.status_code, ": trip status_code"
print get_trip
"""