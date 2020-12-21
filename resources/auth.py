from flask_restful import Resource, reqparse
from database import User
from validations.auth import loginV, registerV


class Login(Resource):
	def post(self):
	
		return ''



class Register(Resource):
	def post(self):
		args = registerV.parse_args()	
		args['roleId'] = 3 # Basic User
		result = User.create(args)

		if(result['code'] == 201):

			return 'Başarılı', result['code']
		else:
			return result['data'], result['code']
