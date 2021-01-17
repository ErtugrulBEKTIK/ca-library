from flask_restful import reqparse

# Validations for book creation route
createV = reqparse.RequestParser()
createV.add_argument("fullName", type=str, help="Please send fullName correctly!", required=True)
createV.add_argument("description", type=str, help="Please send description correctly!")

# Validations for book creation route
updateV = reqparse.RequestParser()
updateV.add_argument("fullName", type=str, help="Please send fullName correctly!", required=True)
updateV.add_argument("description", type=str, help="Please send description correctly!")

# Validations for book list route
listV = reqparse.RequestParser()
listV.add_argument("pageSize", type=int, location='args')
listV.add_argument("pageNumber", type=int, location='args')
listV.add_argument("status", type=int, location='args')
