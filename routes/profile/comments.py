from flask_restful import request, Resource
from database import Comment
from validations.profile import bookCommentV, saveCommentV, deleteWishV


class ProfileComments(Resource):
	def get(self):
		args = bookCommentV.parse_args()	
		args['userId'] = request.environ['decoded']['id']
		
		result = Comment.getUserComment(args)
		return result['data'], result['code']

	def post(self):
		args = saveCommentV.parse_args()
		args['userId'] = request.environ['decoded']['id']
		
		result = Comment.create(args)
		return result['data'], result['code']

	def patch(self):
		args = saveCommentV.parse_args()
		args['userId'] = request.environ['decoded']['id']
		
		result = Comment.updateByUser(args)
		return result['data'], result['code']

	def delete(self):
		args = deleteWishV.parse_args()	
		userId = request.environ['decoded']['id']
		
		result = Wish.delete(userId, args['wishId'])
		return result['data'], result['code']

