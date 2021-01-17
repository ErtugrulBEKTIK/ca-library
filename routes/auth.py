from flask_restful import Resource, reqparse
from database import User
from validations.auth import loginV, registerV
from passlib.hash import sha256_crypt
from settings import api_key
import jwt

class Login(Resource):
	def post(self):

		args = loginV.parse_args()	
		result = User.getByEmail(args['email'])

		# User not found
		if(result['code'] == 404):
			return None, 401

		# If password not match
		if(not sha256_crypt.verify(args['password'], result['data']['password'])):
			return None, 401

		# Generate token
		encoded_jwt = jwt.encode(
			{
				'id': result['data']['id'],
				'email': result['data']['email'],
				'roleId': result['data']['roleId']
			}, 
			api_key
		)

		return {
			'firstName': result['data']['firstName'],
			'lastName': result['data']['lastName'],
			'roleId': result['data']['roleId'],
			'email': result['data']['email'],
			'avatar': result['data']['avatar'],
			'token': encoded_jwt.decode('utf-8')
		}



class Register(Resource):
	def post(self):
		args = registerV.parse_args()	
		args['password'] = sha256_crypt.encrypt(args['password'])
		args['roleId'] = 3 # Basic User
		result = User.create(args)

		if(result['code'] == 201):

			encoded_jwt = jwt.encode(
			{
				'id': result['data']['userId'],
				'email': args['email'],
				'roleId': 3
			}, 
			api_key
			)

			return {
				'firstName': args['firstName'],
				'lastName': args['lastName'],
				'roleId': args['roleId'],
				'email': args['email'],
				'avatar': '001-boy.svg',
				'token': encoded_jwt.decode('utf-8')
			}
		else:
			return result['data'], result['code']
