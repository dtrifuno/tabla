from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_pyfile('setting.cfg')
db = MongoEngine(app)
jwt = JWTManager(app)
CORS(app, expose_headers='Authorization')
api = Api(app)

from tabla_server import models, resources, views
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.Tables, '/tables')
api.add_resource(resources.Table, '/table')
api.add_resource(resources.GetDeleteTable, '/table/<table_id>')
api.add_resource(resources.Column, '/column')
api.add_resource(resources.DeleteColumn, '/column/<column_id>')
api.add_resource(resources.Entry, '/entry')
api.add_resource(resources.DeleteEntry, '/entry/<entry_id>')
