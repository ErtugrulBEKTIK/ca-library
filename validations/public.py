from flask_restful import reqparse

# Validations for book list route
booksV = reqparse.RequestParser()
booksV.add_argument("pageSize", type=int)
booksV.add_argument("pageNumber", type=int)
booksV.add_argument("search", type=str)
booksV.add_argument("categories", type=int, action='append')

# Validations for comment list route
commentsV = reqparse.RequestParser()
commentsV.add_argument("pageSize", type=int, location='args')
commentsV.add_argument("pageNumber", type=int, location='args')