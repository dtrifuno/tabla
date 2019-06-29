from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api

app = Flask(__name__)
app.config.from_pyfile('setting.cfg')
db = MongoEngine(app)
print(dir(db))
api = Api(app)

from tabla_server import models, resources, views
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')
