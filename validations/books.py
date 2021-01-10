from flask_restful import reqparse

# Validations for book creation route
createV = reqparse.RequestParser()

createV.add_argument("title", type=str, help="Please send title correctly!", required=True)
createV.add_argument("authors", type=dict, help="Please send authors correctly!", action='append', required=True)
createV.add_argument("categories", type=dict, help="Please send categories correctly!", action='append', required=True)
createV.add_argument("publisher", type=str, help="Please send publisher correctly!")
createV.add_argument("year", type=str, help="Please send year correctly!")
createV.add_argument("shelf", type=str, help="Please send shelf correctly!")
createV.add_argument("barcode", type=str, help="Please send barcode correctly!")
createV.add_argument("description", type=str, help="Please send description correctly!")

# Validations for book creation route
updateV = reqparse.RequestParser()

updateV.add_argument("title", type=str, help="Please send title correctly!", required=True)
updateV.add_argument("authors", type=dict, help="Please send authors correctly!", action='append', required=True)
updateV.add_argument("categories", type=dict, help="Please send categories correctly!", action='append', required=True)
updateV.add_argument("publisher", type=str, help="Please send publisher correctly!")
updateV.add_argument("year", type=str, help="Please send year correctly!")
updateV.add_argument("shelf", type=str, help="Please send shelf correctly!")
updateV.add_argument("barcode", type=str, help="Please send barcode correctly!")
updateV.add_argument("description", type=str, help="Please send description correctly!")


# Validations for book list route
listV = reqparse.RequestParser()
listV.add_argument("pageSize", type=int, location='args')
listV.add_argument("pageNumber", type=int, location='args')
listV.add_argument("search", type=str, location='args')