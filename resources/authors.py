from flask_restful import Resource, reqparse
from database import Author
from validations.authors import createV



class AuthorsApi(Resource):
	def get(self):

		return Author.getAll()

	def post(self):
		args = createV.parse_args()	
		Author.create(args)
		return args



class AuthorApi(Resource):
	def get(self, authorId):
		return Author.getById(authorId)