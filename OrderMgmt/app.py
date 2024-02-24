from flask import Flask, jsonify, request
#from flask_restful import Resource, Api
from flask_cors import CORS
from flask_restx import Namespace, Api, Resource

from Route import order_routes
from OrderMgmt import OrderMgmt#, order_ns

app = Flask(__name__, static_url_path='/', static_folder='/ui', instance_relative_config=True)
CORS(app, resources={r"/api/*": {"origins":"*"}})
#app.register_blueprint(order_routes)
api = Api(app, doc="/swagger")
#api = Api(app)
todos = {}

@app.route('/api/v1/testdeploy')
def resmsg():
        return 'Successfully Deployed!', 201

api.add_resource(OrderMgmt, '/api/v1/order')

if __name__ == '__main__':
    app.run(debug=True)