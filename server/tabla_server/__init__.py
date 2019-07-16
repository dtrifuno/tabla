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
api.add_resource(resources.UserRegistration, '/api/register')
api.add_resource(resources.UserLogin, '/api/login')

api.add_resource(resources.Tables, '/api/tables')

api.add_resource(resources.PostTable, '/api/table')
api.add_resource(resources.Table, '/api/table/<table_id>')

api.add_resource(resources.PostColumn, '/api/column')
api.add_resource(resources.Column, '/api/column/<column_id>')

api.add_resource(resources.PostEntry, '/api/entry')
api.add_resource(resources.Entry, '/api/entry/<entry_id>')
