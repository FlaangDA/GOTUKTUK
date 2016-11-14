import httplib, json, requests


def post():
	headers = {'Content-type' : 'application/json'}
	url = 'http://127.0.0.1:8000/create_customer/'
	json_data = { "lastname" : "Chang", "firstname" : "Hannns", "email" : "hans_ccc40@gmail.com",  "password1" : "267ec600500",  "password2" : "267ec600500",  "phone" : "95936294", "dob" : "2016-01-17", "nationality" : "Norwegian", "facebookurl" : "facebook.com"}
	r = requests.post(url, json.dumps(json_data), headers=headers)

	print r.content

if __name__ == '__main__':
	post()