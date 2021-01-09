from flask_restful import reqparse

# Validations for login route
loginV = reqparse.RequestParser()
loginV.add_argument("email", type=str, help="Please send email correctly!", required=True)
loginV.add_argument("password", type=str, help="Please send password correctly!", required=True)

# Validations for register route
registerV = reqparse.RequestParser()
registerV.add_argument("firstName", type=str, help="Please send firstName correctly!", required=True)
registerV.add_argument("lastName", type=str, help="Please send lastName correctly!", required=True)
registerV.add_argument("email", type=str, help="Please send email correctly!", required=True)
registerV.add_argument("password", type=str, help="Please send password correctly!", required=True)

# Validations for register route
checkAuthV = reqparse.RequestParser()
checkAuthV.add_argument("Authorization", type=str, help="Token!", location='headers')
