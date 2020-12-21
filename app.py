from flask import Flask, request
from flask_restful import Api, Resource

from resources.routes import initialize_routes
from middlewares import initialize_middlewares

app = Flask(__name__)
api = Api(app)

initialize_middlewares(app)
initialize_routes(api)


if __name__ == '__main__':
	app.run(debug=True)