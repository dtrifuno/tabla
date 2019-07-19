from flask import Flask, Blueprint, render_template
from flask_mongoengine import MongoEngine
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_pyfile('setting.cfg')
db = MongoEngine(app)
jwt = JWTManager(app)
CORS(app, expose_headers='Authorization')

client_bp = Blueprint('client_app', __name__,
                      url_prefix='/',
                      static_url_path='',
                      static_folder='./public',
                      template_folder='./public')


@client_bp.route('/')
def index():
    return render_template('index.html')


app.register_blueprint(client_bp)

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

from tabla_server import models, resources, views
api.add_resource(resources.UserRegistration, '/register')
api.add_resource(resources.UserLogin, '/login')

api.add_resource(resources.Tables, '/tables')

api.add_resource(resources.PostTable, '/table')
api.add_resource(resources.Table, '/table/<table_id>')

api.add_resource(resources.PostColumn, '/column')
api.add_resource(resources.Column, '/column/<column_id>')

api.add_resource(resources.PostEntry, '/entry')
api.add_resource(resources.Entry, '/entry/<entry_id>')
app.register_blueprint(api_bp)
