import json

from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from passlib.hash import pbkdf2_sha256

from tabla_server import db
from tabla_server import models


user_parser = reqparse.RequestParser()
user_parser.add_argument('email', required=True)
user_parser.add_argument('password', required=True)


class UserRegistration(Resource):
    def post(self):
        data = user_parser.parse_args()
        print(f'got a post to /registration - {data}')
        user_exists = models.User.objects(email=data['email'])
        if user_exists:
            return {
                'message': f'{data["email"]} is already registered.'}, 500
        new_user = models.User(
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
        data = user_parser.parse_args()
        print(f'got a post to /login - {data}')
        current_user = models.User.objects(email=data['email']).first()
        if current_user is not None:
            validated = pbkdf2_sha256.verify(data['password'],
                                             current_user.password)
        if current_user is None or not validated:
            return {'message': 'invalid credentials'}, 401

        access_token = create_access_token(identity=data['email'])
        return {'message': f'Logged in as {current_user.email}', 'access_token': access_token}


class Tables(Resource):
    @jwt_required
    def get(self):
        print(f'got a get to /tables')
        current_user = models.User.objects(email=get_jwt_identity()).first()
        tables = models.Table.objects(owner=current_user)
        if tables:
            return tables.to_json()
        else:
            {}, 500


class GetDeleteTable(Resource):
    @jwt_required
    def get(self, table_id):
        print(f'got a get to /table/{table_id}')
        current_user = models.User.objects(email=get_jwt_identity()).first()
        if current_user:
            table = models.Table.objects(id=table_id).first()
            return table.to_json()
        else:
            {}, 500

    @jwt_required
    def delete(self, table_id):
        print(f'got a delete to /table/{table_id}')
        current_user = models.User.objects(email=get_jwt_identity()).first()
        table = models.Table.objects(
            id=table_id, owner=current_user).first()
        if table:
            table.delete()
            return {}
        else:
            return {}, 500


parser = reqparse.RequestParser()
parser.add_argument('tableName')
parser.add_argument('tableId')
parser.add_argument('columnName')
parser.add_argument('columnId')
parser.add_argument('entryName')
parser.add_argument('entryId')


class Table(Resource):
    @jwt_required
    def post(self):
        data = parser.parse_args()
        print(data)
        current_user = models.User.objects(email=get_jwt_identity()).first()
        print(f'got a post to /table - {data}')
        if current_user is not None:
            new_table = models.Table(
                name=data['tableName'], owner=current_user)
            new_table.save()
            return new_table.to_json()
        else:
            return {}, 500

    @jwt_required
    def put(self):
        current_user = models.User.objects(email=get_jwt_identity()).first()
        return {
            'answer': 42
        }


class Column(Resource):
    @jwt_required
    def post(self):
        data = parser.parse_args()
        print(f'got a post to /column')
        current_user = models.User.objects(email=get_jwt_identity()).first()
        table = models.Table.objects(
            owner=current_user, id=data['tableId']).first()
        if not table:
            return {}, 500
        column = models.Column(name=data['columnName'], table=table)
        column.save()
        return column.to_json()

    @jwt_required
    def put(self):
        current_user = models.User.objects(email=get_jwt_identity()).first()
        return {
            'answer': 42
        }


class DeleteColumn(Resource):
    @jwt_required
    def delete(self, column_id):
        current_user = models.User.objects(email=get_jwt_identity()).first()
        column = models.Column.objects(
            id=column_id, owner=current_user).first()
        if column:
            column.delete()
            return {}
        else:
            return {}, 500


class Entry(Resource):
    @jwt_required
    def post(self):
        current_user = models.User.objects(email=get_jwt_identity()).first()
        return {
            'answer': 42
        }

    @jwt_required
    def put(self):
        current_user = models.User.objects(email=get_jwt_identity()).first()
        return {
            'answer': 42
        }


class DeleteEntry(Resource):
    @jwt_required
    def delete(self, entry_id):
        current_user = models.User.objects(email=get_jwt_identity()).first()
        entry = models.Entry.objects(id=entry_id, owner=current_user).first()
        if entry:
            entry.delete()
            return {}
        else:
            return {}, 500
