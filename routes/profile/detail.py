from flask_restful import request, Resource
from database import User
from validations.profile import detailV


class ProfileDetail(Resource):
	def patch(self):
		args = detailV.parse_args()	
		userId = request.environ['decoded']['id']
		result = User.updateById(userId, args)
		return result['data'], result['code']
