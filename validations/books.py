from flask_restful import reqparse

# Validations for book creation route
createV = reqparse.RequestParser()

createV.add_argument("title", type=str, help="Please send title filed correctly!", required=True)
createV.add_argument("authorId", type=int, help="Please send authorId filed correctly!", required=True)
createV.add_argument("description", type=str, help="Please send description filed correctly!")
createV.add_argument("publisher", type=str, help="Please send publisher filed correctly!")
createV.add_argument("year", type=int, help="Please send year filed correctly!")
