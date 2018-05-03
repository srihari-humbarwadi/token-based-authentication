import requests
import secrets
import string
from pprint import pprint

AUTH = 'http://localhost:80/auth'
API = 'http://localhost:80/myapi'
tokensList ={}
msgAuth = ''
msgAPI = ''
API_RESULT = ''


def auth():
	global tokensList
	global msgAuth
	payload = {
		'userid': 'srihari',
		'passwd': '123'
	}

	res = requests.post(AUTH,payload).json()
	msgAuth = res['msg']
	if res['success'] and res['Authenticated']: 
		tokensList = res['tokensList']
		return True
	else:
		return False
	


def auth_token():
	global msgAPI
	global API_RESULT
	validToken = False
	index = str(secrets.randbelow(10))
	payload = {
	'token': index + tokensList[index],
	'API_REQ_DATA': 'GET SECRET MESSAGE'
	}
	print(index + tokensList[index])
	res = requests.post(API, payload).json()
	if res['success']:
		validToken = res['validToken']
	msgAPI = res['msg']
	if validToken:
		tokensList[index] = res['srvToken'][1:]
		API_RESULT = res['API_RESP_DATA']
		return True
	else:
		return False	
if auth():
	while auth_token():
		print(msgAPI)
		#print(API_RESULT)

