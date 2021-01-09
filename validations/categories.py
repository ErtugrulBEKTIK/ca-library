from flask_restful import reqparse

# Validations for category creation route
createV = reqparse.RequestParser()
createV.add_argument("name", type=str, help="Please send name correctly!", required=True)


# Validations for category creation route
updateV = reqparse.RequestParser()
updateV.add_argument("name", type=str, help="Please send name correctly!", required=True)

# Validations for category list route
listV = reqparse.RequestParser()
listV.add_argument("pageSize", type=int, location='args')
listV.add_argument("pageNumber", type=int, location='args')
listV.add_argument("search", type=str, location='args')