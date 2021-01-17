from flask_restful import Resource
from database import Book, Category, Comment
from validations.public import booksV, commentsV


class PublicBooks(Resource):
	def post(self):
		args = booksV.parse_args()	
		result = Book.getAll(args);
		return result['data'], result['code']

class PublicCategories(Resource):
	def get(self):
		result = Category.getAll();
		return result['data'], result['code']


class PublicComments(Resource):
	def get(self, bookId):
		args = commentsV.parse_args()	
		args['bookId'] = bookId
		print(args)
		result = Comment.getBookComments(args);
		return result['data'], result['code']
