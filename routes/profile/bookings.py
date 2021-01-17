from flask_restful import request, Resource
from database import Booking
from validations.profile import bookingListV, borrowV, returnV


class ProfileBookings(Resource):
	def get(self):
		args = bookingListV.parse_args()	
		args['userId'] = request.environ['decoded']['id']
		print(args['userId'])
		result = Booking.getAll(args)
		return result['data'], result['code']

	def post(self):
		args = borrowV.parse_args()	
		userId = request.environ['decoded']['id']
		bookId = args['bookId']
		
		result = Booking.borrowBook(userId, bookId)
		return result['data'], result['code']

	def patch(self):
		args = returnV.parse_args()	
		userId = request.environ['decoded']['id']
		
		result = Booking.returnBook(userId, args['bookingId'])
		return result['data'], result['code']

