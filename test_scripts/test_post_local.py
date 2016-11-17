import httplib, json, requests

import requests, json

#driver: henrik.brownee@gmail.com
#customer: henrik.borthen@gmail.com

driverSession = requests.Session()
customerSession = requests.Session()

json_data = {
	"lastname" : "Sjoetveit", 
	"firstname" : "Sveinung", 
	"email" : "sveinung.Sjoetveitttttt@gmail.com", 
	"dob" : "2016-01-17", 
	"phone" : "98237897", 
	"facebookurl" : "www.facebook.com", 
	"password1" : "267ec600500", 
	"password2" : "267ec600500"
}
create_driver = driverSession.post("http://103.227.177.206:8000/create_driver/", json.dumps(json_data))

print create_driver.status_code, create_driver.text