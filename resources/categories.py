from flask_restful import Resource
from database import Category
from validations.categories import createV, updateV, listV


class CategoriesApi(Resource):
	def get(self):
		args = listV.parse_args()	
		result = Category.getPaginated(args)
		return result['data'], result['code']

	def post(self):
		args = createV.parse_args()	
		Category.create(args)
		return args



class CategoryApi(Resource):
	def get(self, categoryId):
		result = Category.getById(categoryId);
		return result['data'], result['code']

	def patch(self, categoryId):
		args = updateV.parse_args()	
		result = Category.updateById(categoryId, args);
		return result['data'], result['code']

	def delete(self, categoryId):
		result = Category.delete(categoryId)
		return result['data'], result['code']