from flask_restful import reqparse

# Validations for book creation route
createV = reqparse.RequestParser()

createV.add_argument("fullName", type=str, help="Please send fullName filed correctly!", required=True)
createV.add_argument("description", type=str, help="Please send description filed correctly!")

