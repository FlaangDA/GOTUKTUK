import requests, json

#driver: taggi@sup.com
#customer: henrik.borthen@gmail.com

driverSession = requests.Session()
customerSession = requests.Session()

#remove trailing slashes on ALL urls
json_data = {
	"lastname" : "Fladbyy",
	"firstname" : "Torgeir",
	"email" : "torgeir.fladbyyy@gmail.com", 
	"password1" : "267ec600500", 
	"password2" : "267ec600500", 
	"phone" : "95936294",
	"dob" : "2016-01-17",
	"nationality" : "Norwegian",
	"facebookurl" : "facebook.com"
}
		
create_customer = customerSession.post("http://127.0.0.1:8000/create_customer", json.dumps(json_data)) 

login_customer_data =  json.dumps({"email" : "torgeir.fladbyyy@gmail.com", "password" : "267ec600500"})
print customerSession.post("http://127.0.0.1:8000/login", data=login_customer_data).status_code

#return proper http response upon invalid user.
login_driver_data = json.dumps({"email" : "taggi@sup.com", "password" : "267ec600500"})
print driverSession.post("http://127.0.0.1:8000/login", data=login_driver_data).status_code

request_trip_data = json.dumps({
	"customer" : "torgeir.fladbyyy@gmail.com",  
	"pickuplat" : "111.12345", 
	"pickuplng" : "111.31232",
	"dropofflat" : "111.12312",
	"dropofflng" : "111.13123",
	"requestedprice" : "10.00", 
	"acceptedprice" : "True" })



print customerSession.post("http://127.0.0.1:8000/request_trip", data=request_trip_data).status_code

print customerSession.get("http://127.0.0.1:8000/check_triprequest").status_code

ping_data = json.dumps({"lon" : "123.12321", "lat" : "321.12314"})

pkeytriprequest = json.loads(driverSession.post("http://127.0.0.1:8000/ping_triprequest", data=ping_data).text)[0].get('pk')

print pkeytriprequest

accept_triprequest_data = json.dumps({
	"customer" : "torgeir.fladbyyy@gmail.com", 
	"driver" : "taggi@sup.com", 
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
	"etakm" : "10.0", 
	"feedback" : "very good", 
	"rating" : "5", 
	"tripcomplete" : "False", 
	"customer_pays" : "20.00"})

print driverSession.post("http://127.0.0.1:8000/accept_triprequest", data=accept_triprequest_data).text

print customerSession.get("http://127.0.0.1:8000/check_triprequest").text


print customerSession.post("http://127.0.0.1:8000/get_driver_details").text

print driverSession.post("http://127.0.0.1:8000/finish_trip").text
