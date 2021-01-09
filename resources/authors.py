from flask_restful import Resource
from database import Author
from validations.authors import createV, updateV, listV


class AuthorsApi(Resource):
	def get(self):
		args = listV.parse_args()	
		result = Author.getAll(args);
		return result['data'], result['code']

	def post(self):
		args = createV.parse_args()	
		Author.create(args)
		return args



class AuthorApi(Resource):
	def get(self, authorId):
		result = Author.getById(authorId);
		return result['data'], result['code']

	def patch(self, authorId):
		args = updateV.parse_args()	
		result = Author.updateById(authorId, args);
		return result['data'], result['code']

	def delete(self, authorId):
		result = Author.delete(authorId)
		return result['data'], result['code']