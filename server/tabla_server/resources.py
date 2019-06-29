import json

from flask_restful import Resource, reqparse
from passlib.hash import pbkdf2_sha256

from tabla_server import db
from tabla_server.models import User


parser = reqparse.RequestParser()
parser.add_argument(
    'email', help='This field cannot be blank', required=True)
parser.add_argument(
    'password', help='This field cannot be blank', required=True)


class UserRegistration(Resource):
    def post(self):
        print(self)
        data = parser.parse_args()
        print(f'got a post to /registration - {data}')
        user_exists = User.objects(email=data['email'])
        if user_exists:
            return {
                'message': f'{data["email"]} is already registered.'}
        new_user = User(
            email=data['email'],
            password=pbkdf2_sha256.hash(data['password'])
        )
        try:
            new_user.save()
            return {
                'message': f'User {data["email"]} was created.',
            }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        search_results = User.objects(email=data['email'])
        if search_results:
            current_user = search_results[0]
            validated = pbkdf2_sha256.verify(data['password'],
                                             current_user.password)
        if not search_results or not validated:
            return {'message': 'invalid credentials'}
        return {'message': f'Logged in as {current_user.email}'}


class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}


class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}


class AllUsers(Resource):
    def get(self):
        return {'message': 'List of users'}

    def delete(self):
        return {'message': 'Delete all users'}


class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }
