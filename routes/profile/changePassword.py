from flask_restful import request, Resource
from database import User
from validations.profile import passwordV
from passlib.hash import sha256_crypt

class ProfilePassword(Resource):
	def patch(self):
		args = passwordV.parse_args()	
		userId = request.environ['decoded']['id']

		#Get user by id in db
		result = User.getPassword(userId)
		
		# If password not match
		if(not sha256_crypt.verify(args['oldPassword'], result['data']['password'])):
			return None, 401

		hashedPass = sha256_crypt.encrypt(args['newPassword'])

		result = User.updatePassword(userId, hashedPass)
		return result['data'], result['code']
