import flask
import json
import secrets
import string
from pymongo import MongoClient

app = flask.Flask(__name__)
tokens = {
	'0':	secrets.token_urlsafe(20),
	'1':	secrets.token_urlsafe(20),
	'2':	secrets.token_urlsafe(20),
	'3':	secrets.token_urlsafe(20),
	'4':	secrets.token_urlsafe(20),
	'5':	secrets.token_urlsafe(20),
	'6':	secrets.token_urlsafe(20),
	'7':	secrets.token_urlsafe(20),
	'8':	secrets.token_urlsafe(20),
	'9':	secrets.token_urlsafe(20)
}
__userid__ = 'srihari'
__passwd__ = '123'

@app.route('/')
def hello():
	return "Hello world"


@app.route('/myapi', methods=['POST'])
def api():
	data = {
		'success': False,
		'API_RESP_DATA': 'THIS IS A SECRET MESSAGE',
		'msg': 'Please send a valid token',
		'validToken':False,
		'srvToken': ''
	}
	if flask.request.method == 'POST':
		if flask.request.form.get('token'):
			tokenTest = flask.request.form.get('token')
			print(flask.request.form.get('API_REQ_DATA'))
			index = tokenTest[0]
			token = tokenTest[1:]
			print(tokens[index] + "   " + token )
			if tokens[index] == token:
				temp = secrets.token_urlsafe(20)
				tokens[index]  = temp
				data['srvToken'] = str(secrets.randbelow(10)) + temp
				print('REQUEST AUTHENTICATED')
				data['success'] = True
				data['validToken'] = True
				data['msg'] = 'Resouce request Authenticated'
				data['API_RESP_DATA'] = 'YOU NOW HAVE ACCESS TO THE SECRET MESSAGE => Hello World'
	return flask.jsonify(data)


@app.route('/auth', methods=['POST'])
def reg():
	data ={
	'success': False,
	'tokensList': {'Authenticated': False},
	'msg': 'Authentication pending',
	'Authenticated': False
	}
	if flask.request.method == 'POST':
		if flask.request.form.get('userid') and flask.request.form.get('passwd'):
			userid = flask.request.form.get('userid')
			passwd = flask.request.form.get('passwd')
			if userid == __userid__ and passwd ==__passwd__:
				data['success'] = True
				data['msg'] = 'Authentication Succeeded'
				data['tokensList'] = tokens
				data['Authenticated'] = True
	return flask.jsonify(data)

if __name__ == "__main__":
	app.run(debug=True, port=80)

