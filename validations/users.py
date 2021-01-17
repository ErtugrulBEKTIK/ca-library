from flask_restful import reqparse

# Validations for book creation route
createV = reqparse.RequestParser()
createV.add_argument("firstName", type=str, help="Please send firstName correctly!", required=True)
createV.add_argument("lastName", type=str, help="Please send lastName correctly!", required=True)
createV.add_argument("email", type=str, help="Please send email correctly!", required=True)
createV.add_argument("roleId", type=str, help="Please send role correctly!", required=True)
createV.add_argument("password", type=str, help="Please send password correctly!", required=True)

# Validations for book creation route
updateV = reqparse.RequestParser()
updateV.add_argument("firstName", type=str, help="Please send firstName correctly!", required=True)
updateV.add_argument("lastName", type=str, help="Please send lastName correctly!", required=True)
updateV.add_argument("email", type=str, help="Please send email correctly!", required=True)
updateV.add_argument("roleId", type=str, help="Please send role correctly!", required=True)

# Validations for book list route
listV = reqparse.RequestParser()
listV.add_argument("pageSize", type=int, location='args')
listV.add_argument("pageNumber", type=int, location='args')
