from flask_restful import request, Resource
from database import Wish
from validations.profile import wishListV, createWishV, deleteWishV


class ProfileWishes(Resource):
	def get(self):
		args = wishListV.parse_args()	
		args['userId'] = request.environ['decoded']['id']
		
		result = Wish.getAll(args)
		return result['data'], result['code']

	def post(self):
		args = createWishV.parse_args()	
		userId = request.environ['decoded']['id']
		bookId = args['bookId']
		
		result = Wish.create(userId, bookId)
		return result['data'], result['code']

	def delete(self):
		args = deleteWishV.parse_args()	
		userId = request.environ['decoded']['id']
		
		result = Wish.delete(userId, args['wishId'])
		return result['data'], result['code']

class ProfileNotifications(Resource):
	def get(self):
		userId = request.environ['decoded']['id']
		
		result = Wish.notifications(userId)
		return result['data'], result['code']