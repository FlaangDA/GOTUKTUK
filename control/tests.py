from django.test import LiveServerTestCase
from django.test import Client
import simplejson, json, os
from datetime import datetime
import base64

from users.models import CustomUser, CustomerDetails, DriverDetails
import django.utils
# Create your tests here.


class TestCalls(LiveServerTestCase):

	def test_all(self):


		c = Client(HTTP_USER_AGENT='Mozilla/5.0')
		c2 = Client()
		c3 = Client()
		c4 = Client()
		c5 = Client(enforce_csrf_checks=True)

		default_pic = base64.encodestring(open('control/dummy_avatar.png', 'rw').read())

		print len(default_pic)
		#create a user

		json_data = {
			"lastname" : "Fladbyy",
			"firstname" : "Torgeir",
			"email" : "torgeir.fladbyy@gmail.com", 
			"password1" : "267ec600500", 
			"password2" : "267ec600500", 
			"phone" : "95936294",
			"dob" : "2016-01-17",
			"nationality" : "Norwegian",
			"facebookurl" : "facebook.com"
		}
		
		create_customer = c.post("/create_customer/", json.dumps(json_data), content_type="application/json") 


		print create_customer.status_code
		print create_customer.content




		json_data = {
			"lastname" : "Borthen",
			"firstname" : "Henrik",
			"email" : "henrik.borthen@gmail.com", 
			"password1" : "267ec600500", 
			"password2" : "267ec600500", 
			"phone" : "95936294",
			"dob" : "2016-01-17",
			"nationality" : "Norwegian",
			"facebookurl" : "facebook.com"
		}
		
		create_customer = c4.post("/create_customer/", json.dumps(json_data), content_type="application/json")

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
			"password2" : "267ec600500"
		}

		create_driver = c2.post("/create_driver/", json.dumps(json_data), content_type="application/json")

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
			"password2" : "267ec600500"
		}

		create_driver = c3.post("/create_driver/", json.dumps(json_data), content_type="application/json")

		print create_driver.status_code
		print create_driver

		#log the user in

		json_data = {"email" : "torgeir.fladbyy@gmail.com", "password" : "267ec600500"}

		login_user = c.post("/login/", json.dumps(json_data), content_type="application/json")
		print login_user.status_code
		print login_user

		json_data = {"profile_pic" : default_pic}
		add_profilepic = c.post("/add_profile_pic/", json.dumps(json_data), content_type="application/json")

		print add_profilepic.status_code
		print add_profilepic


		json_data = {"email" : "henrik.borthen@gmail.com", "password" : "267ec600500"}

		login_user = c4.post("/login/", json.dumps(json_data), content_type="application/json")
		print login_user.status_code
		print login_user


		
		"""
		json_data = {"email" : "torgeir.fladbyy@gmail.com", "password" : "267ec600500"}

		logout = c.post("/logout/", json.dumps(json_data), content_type="application/json")
		print logout.status_code
		print "Logout status code: ", logout
		"""
		json_data = {"email" : "henrik.browne@gmail.com", "password" : "267ec600500" }

		login_user = c2.post("/login/", json.dumps(json_data), content_type="application/json")
		print login_user.status_code
		print login_user

		json_data = {"email" : "sveinung.Sjoetveit@gmail.com", "password" : "267ec600500"}

		login_user = c3.post("/login/", json.dumps(json_data), content_type="application/json")

		print login_user.status_code
		print login_user


		json_data = {"email" : "henrik.browne@gmail.com"}

		disable = c2.post("/disable_driver/", json.dumps(json_data), content_type="application/json")
		print disable.status_code
		print disable


		json_data = {"email" : "henrik.browne@gmail.com"}

		enable = c2.post("/enable_driver/", json.dumps(json_data), content_type="application/json")
		print enable.status_code
		print enable

		json_data = {"etakm" : 5, "bs" : "faenda"}
		check_price = c.post("/check_price", json.dumps(json_data), content_type="application/json")
		print check_price.status_code
		print "Price for a trip: ", check_price.content

		available_drivers = c.get("/available_drivers/")
		print available_drivers.status_code
		print "available drivers: ", available_drivers.json()

		json_data = {
			"customer" : "torgeir.fladbyy@gmail.com",  
			"pickuplat" : "111.12345", 
			"pickuplng" : "111.31232",
			"dropofflat" : "111.12312",
			"dropofflng" : "111.13123",
			"requestedprice" : "4.00", 
			"acceptedprice" : "True"
		}
		request_trip = c.post("/request_trip/", json.dumps(json_data), content_type="application/json")
		json_data = {
			"customer" : "henrik.borthen@gmail.com",  
			"pickuplat" : "111.12345", 
			"pickuplng" : "111.31232",
			"dropofflat" : "111.12312",
			"dropofflng" : "111.13123",
			"requestedprice" : "4.00", 
			"acceptedprice" : "True"
		} 
		print request_trip

		print "FIRST CHECK TRIPREQUEST"

		jdata = json.loads(request_trip.content)

		#pkeytriprequest = jdata[1]


		#print "request trip: ", request_trip.content, pkeytriprequest
		"""
		json_data = {
			"triprequestID" : pkeytriprequest,

		}"""

		check_triprequest = c.get("/check_triprequest/")

		print check_triprequest.content

		json_data = {"lon" : "123.12321", "lat" : "321.12314"}

		ping_triprequest = c3.post("/ping_triprequest/", json.dumps(json_data), content_type="application/json")
		print ping_triprequest
		print "ping ping_triprequest: ", ping_triprequest.content

		pkeytriprequest = json.loads(ping_triprequest.content)[0].get('pk')

		print pkeytriprequest

		print type(pkeytriprequest)

		print pkeytriprequest

		json_data={
			"customer" : "torgeir.fladbyy@gmail.com", 
			"driver" : "sveinung.Sjoetveit@gmail.com", 
			"tripreqID" : pkeytriprequest,
			"pickuplat" : "11.12345", 
			"pickuplng" : "11.31232",
			"dropofflat" : "11.12312",
			"dropofflng" : "11.13123",
			"datetimetrip" : "2016-01-12 14:59:49", 
			"timeconsumed" : "00:00:00", 
			"tripstartdatetime": "2016-01-12 15:00:00", 
			"triporderdatetime" : "2016-01-12 15:00:00", 
			"etaarrival": "15:15:00", 
			"etatrip" : "00:15:00", 
			"etakm" : "5.0", 
			"feedback" : "very good", 
			"rating" : "5", 
			"tripcomplete" : "False", 
			"customer_pays" : "20.00",
		}

		print json_data

		print json.dumps(json_data)
		accept_trip = c3.post("/accept_triprequest/", json.dumps(json_data), content_type="application/json")

		print accept_trip

		print "SECOND CHECK TRIPREQUEST"

		json_data = {
			"triprequestID" : pkeytriprequest,

		}

		check_triprequest = c.get("/check_triprequest/")

		print check_triprequest.content

		get_driver_details = c.post("/get_driver_details/", json.dumps({"driver" : "sveinung.Sjoetveit@gmail.com"}), content_type="application/json")

		print get_driver_details

		get_trip_graphics = c.get("/get_trip_graphics")
		print get_trip_graphics, get_trip_graphics.content

		finish_trip = c3.post("/finish_trip/")
		print finish_trip.status_code
		print finish_trip, finish_trip.content
		module_dir = os.path.dirname(__file__)
		filename = os.path.join(module_dir, 'testimages/pin_location.png')

		with open(filename) as img:
			json_data = {
				"name" : "packagedeal1",
				"header_image" : img,
				"description" : "some description",
				"price" : 50,
				"time_first_from" : "2016-01-12 14:59:49",
				"time_first_to" : "2016-01-12 14:59:49",
				"time_second_from" : "2016-01-12 14:59:49",
				"time_second_to" : "2016-01-12 14:59:49",
				"pickuppoint" : "0000.0000",
				"dropoffpoint" : "0000.0000",
			}
			postres = c.post("/create_packagedeal/", json.dumps(json_data), content_type="application/json")
			getres = c.get("/get_packagedeals/")
			print postres.content, getres.content

#class TestStatic(StaticLiveServerTestCase)

	
	#def testFileUpload(self):



			
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