from flask_restful import Resource
from database import Book, Category
from validations.public import booksV


class PublicBooks(Resource):
	def post(self):
		args = booksV.parse_args()	
		result = Book.getAll(args);
		return result['data'], result['code']



class PublicCategories(Resource):
	def get(self):
		result = Category.getAll();
		return result['data'], result['code']
