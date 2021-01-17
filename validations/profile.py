from flask_restful import reqparse

# Validations for profile edit route
detailV = reqparse.RequestParser()
detailV.add_argument("firstName", type=str)
detailV.add_argument("lastName", type=str)
detailV.add_argument("email", type=str)
detailV.add_argument("avatar", type=str)


# Validations for password change route
passwordV = reqparse.RequestParser()
passwordV.add_argument("oldPassword", type=str)
passwordV.add_argument("newPassword", type=str)
passwordV.add_argument("reNewPassword", type=str)

# Validations for borrow route
borrowV = reqparse.RequestParser()
borrowV.add_argument("bookId", type=str)

# Validations for booking list route
bookingListV = reqparse.RequestParser()
bookingListV.add_argument("pageSize", type=int, location='args')
bookingListV.add_argument("pageNumber", type=int, location='args')

# Validations for return book route
returnV = reqparse.RequestParser()
returnV.add_argument("bookingId", type=str)

# Validations for create wish route
createWishV = reqparse.RequestParser()
createWishV.add_argument("bookId", type=str)

# Validations for wish list route
wishListV = reqparse.RequestParser()
wishListV.add_argument("pageSize", type=int, location='args')
wishListV.add_argument("pageNumber", type=int, location='args')

# Validations for delete wish
deleteWishV = reqparse.RequestParser()
deleteWishV.add_argument("wishId", type=str, location='args')

# Validations for create comment route
saveCommentV = reqparse.RequestParser()
saveCommentV.add_argument("star", type=str)
saveCommentV.add_argument("content", type=str)
saveCommentV.add_argument("bookId", type=str)

# Validations for get book comment route
bookCommentV = reqparse.RequestParser()
bookCommentV.add_argument("bookId", type=str, location='args')