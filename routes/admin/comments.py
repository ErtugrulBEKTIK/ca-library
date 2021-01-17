from flask_restful import Resource
from database import Comment
from validations.comments import createV, updateV, listV


class AdminComments(Resource):
	def get(self):
		args = listV.parse_args()	
		result = Comment.getAll(args);
		return result['data'], result['code']

class AdminComment(Resource):

	def delete(self, commentId):
		result = Comment.delete(commentId)
		return result['data'], result['code']

	def patch(self, commentId):
		result = Comment.approve(commentId)
		return result['data'], result['code']