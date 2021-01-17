from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from router import initialize_routes
from middlewares import initialize_middlewares

app = Flask(__name__)

cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


api = Api(app)
initialize_middlewares(app)
initialize_routes(api)


if __name__ == '__main__':
	app.run(debug=True)