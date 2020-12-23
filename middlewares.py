from flask import request, Response
import jwt
from settings import api_key
from validations.auth import checkAuthV

def initialize_middlewares(app):
  @app.before_request
  def checkAuth():
    namespace = request.path.split('/')[1]
    if request.method != 'OPTIONS' and namespace == 'admin':
      args = checkAuthV.parse_args()

      if args.Authorization == None:
        return Response('Token not provided', 422)
      
      # Remove 'Bearer ' string in front of the token
      token = args.Authorization[7:]

      try:
        jwt.decode(token, api_key)
      except:
        return Response('Token not validated', 401)
      
  

      
  