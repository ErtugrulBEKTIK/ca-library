from flask import request

def initialize_middlewares(app):
  @app.before_request
  def checkAuth():
    if request.path[0:4] == '/api':
      print(request)
      
  

      
  