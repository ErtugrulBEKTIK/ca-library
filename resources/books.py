from flask_restful import Resource, reqparse
from database import Book
from validations.books import createV, listV



class BooksApi(Resource):
	def get(self):
		args = listV.parse_args()	
		result = Book.getAll(args)
		return result['data'], result['code']

	def post(self):
		args = createV.parse_args()	
		result = Book.create(args)
		return result['data'], result['code']



class BookApi(Resource):
	def get(self, bookId):
		result = Book.getById(bookId)
		return result['data'], result['code']

	def delete(self, bookId):
		result = Book.delete(bookId)
		return result['data'], result['code']