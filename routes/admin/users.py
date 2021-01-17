from flask_restful import Resource
from database import User
from validations.users import createV, updateV, listV


class AdminUsers(Resource):
	def get(self):
		args = listV.parse_args()	
		result = User.getBasicUsers(args);
		return result['data'], result['code']

	def post(self):
		args = createV.parse_args()	
		User.create(args)
		return args



class AdminUser(Resource):
	def get(self, userId):
		result = User.getById(userId);
		return result['data'], result['code']

	def patch(self, userId):
		args = updateV.parse_args()	
		result = User.updateByAdmin(userId, args);
		return result['data'], result['code']

	def delete(self, userId):
		result = User.delete(userId)
		return result['data'], result['code']

class AdminList(Resource):
	def get(self):
		result = User.getAdmins();
		return result['data'], result['code']
