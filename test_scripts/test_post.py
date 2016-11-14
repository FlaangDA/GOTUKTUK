

import httplib, json, requests


def post():
	headers = {'Content-type' : 'application/json'}
	url = 'http://103.227.177.206:8000/create_customer/'
	
	json_data = {
	"lastname" : "Fladbyy",
	"firstname" : "Torgeir",
	"email" : "torgeir.fladbyyy@gmail.com", 
	"password1" : "267ec600500", 
	"password2" : "267ec600500", 
	"phone" : "95936294",
	"dob" : "2016-01-17",
	"nationality" : "Norwegian",
	"facebookurl" : "facebook.com"}

	r = requests.post(url, json.dumps(json_data), headers=headers)

	print r.content

	#Skal returnere Etternavn Fornavn


	json_data = {"lastname" : "Borthen",
	"firstname" : "Henrik",
	"email" : "henrik.borthen@gmail.com", 
	"password1" : "267ec600500", 
	"password2" : "267ec600500", 
	"phone" : "95936294",
	"dob" : "2016-01-17",
	"nationality" : "Norwegian",
	"facebookurl" : "facebook.com"}

	r = requests.post(url, json.dumps(json_data), headers=headers)

	print r.content

	#Skal returnere Etternavn Fornavn

	json_data = {
	"lastname" : "Browne", 
	"firstname" : "Henrik", 
	"email" : "henrik.brownee@gmail.com", 
	"dob" : "2016-01-17", 
	"phone" : "98237897", 
	"facebookurl" : "www.facebook.com", 
	"password1" : "267ec600500",
	"password2" : "267ec600500"}


	url = 'http://103.227.177.206:8000/create_driver/'

	r = requests.post(url, json.dumps(json_data), headers=headers)

	#Skal returnere Etternavn Fornavn

	json_data = {"email" : "torgeir.fladbyyy@gmail.com", "password" : "267ec600500"}

	url = 'http://103.227.177.206:8000/login/'

	r = requests.post(url, json.dumps(json_data), headers=headers)

	print r.content

	#Skal returnere User is now logged in.

	json_data = {"email" : "henrik.brownee@gmail.com", "password" : "267ec600500" }

	r = requests.post(url, json.dumps(json_data), headers=headers)

	print r.content

	#Skal returnere User is now logged in.

	url = 'http://103.227.177.206:8000/logout/'

	json_data = {"email" : "henrik.brownee@gmail.com", "password" : "267ec600500" }

	#r = requests.post(url, json.dumps(json_data), headers=headers)

	print r.content

	#Skal returnere User logged out. 
	url = 'http://103.227.177.206:8000/disable_driver/'

	r = requests.post(url, json.dumps(json_data), headers=headers)

	print r.content

	#For at denne skal fungere ma klienten ha en aktiv session med server.
	#Stateless requests fungerer altsaa ikke her, tror vi maa bruke keep-alive http.

	url = 'http://103.227.177.206:8000/enable_driver/'

	r = requests.post(url, json.dumps(json_data), headers=headers)

	print r.content


	#For at denne skal fungere maa klienten ha en aktiv session med server.
	#Stateless requests fungerer altsa ikke her, tror vi ma bruke keep-alive http.

	url = 'http://103.227.177.206:8000/available_drivers/'

	r = requests.get(url, json.dumps(json_data), headers=headers)
	#Fungerer ikke helt som den skal, men burde uansett returnere en liste
	#med alle sjaforene som er lagret. 

	print r.content

	json_data = {
			"customer" : "torgeir.fladbyyy@gmail.com", 
			"pickuplat" : "111.12345", 
			"pickuplng" : "111.31232",
			"dropofflat" : "111.12312",
			"dropofflng" : "111.13123",
			"requestedprice" : "4.00", 
			"acceptedprice" : "True"
		}

	url = 'http://103.227.177.206:8000/request_trip/'


	r = requests.post(url, json.dumps(json_data), headers=headers)

	print r.content
	
	json_data={
			"customer" : "torgeir.fladbyyy@gmail.com", 
			"driver" : "henrik.brownee@gmail.com", 
			"pickuplat" : "111.12345", 
			"pickuplng" : "111.31232",
			"dropofflat" : "111.12312",
			"dropofflng" : "111.13123",
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
			"customer_pays" : "20.00"
		}

	url = 'http://103.227.177.206:8000/accept_triprequest/'

	#Det er altsa driver som kan accepte et triprequest
	r = requests.post(url, json.dumps(json_data), headers=headers)

	print r.content

if __name__ == '__main__':

	post()