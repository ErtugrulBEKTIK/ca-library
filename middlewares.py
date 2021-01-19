from flask import request, Response
import jwt
from settings import api_key
from validations.auth import checkAuthV

def initialize_middlewares(app):
  @app.before_request
  def checkAuth():
    namespace = request.path.split('/')[1]
    if request.method != 'OPTIONS' and (namespace == 'admin' or namespace == 'profile'):
      args = checkAuthV.parse_args()

      if args.Authorization == None:
        return Response('Token not provided', 422)
      
      # Remove 'Bearer ' string in front of the token
      token = args.Authorization[7:]

      try:
        decoded = jwt.decode(token, api_key)
        request.environ['decoded'] = decoded

      except Exception as err:
        raise err
        return Response('Token not validated', 401)

      # Security check for admin privileges
      if namespace == 'admin' and not (decoded['roleId'] == 1 or decoded['roleId'] == 2):
        return Response('You are not allowed to enter', 401)

      
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Origin', '*')
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
      return response
  

      
  