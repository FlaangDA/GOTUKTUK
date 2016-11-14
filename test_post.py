

import httplib, json, requests


def post():
	headers = {'Content-type' : 'application/json'}
	url = '103.227.177.026:8000/create_customer/'
	json_data = { "lastname" : "Fladbyy", "firstname" : "Torgeir", "email" : "torgeir.fladbyy@gmail.com",  "password1" : "267ec600500",  "password2" : "267ec600500",  "phone" : "95936294", "dob" : "2016-01-17", "nationality" : "Norwegian", "facebookurl" : "facebook.com"}
	r = requests.post(url, data=json.dumps(json_data), headers=headers)

	print r

if __name__ == '__main__':
	post()