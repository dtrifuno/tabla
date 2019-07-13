import json
from bson import ObjectId

from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from passlib.hash import pbkdf2_sha256

from tabla_server import db
from tabla_server import models


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


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
        print(current_user, type(current_user))
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
            return JSONEncoder().encode([table.header_to_client() for table in tables])
        else:
            {}, 500

    @jwt_required
    def put(self):
        print(f'got a get to /tables - {request.json}')
        tables_request = request.json.get('tables', None)
        if tables_request is None:
            return {}, 500
        table_ids = [x['id'] for x in tables_request]
        tables = models.Table.objects(id__in=table_ids)
        for table in tables:
            new_order = next(x['order']
                             for x in tables_request if x['id'] == str(table.id))
            table.order = new_order
            table.save()
        return {}


parser = reqparse.RequestParser()
parser.add_argument('tableId')
parser.add_argument('columnId')
parser.add_argument('name')
parser.add_argument('order', type=int)


class Table(Resource):
    @jwt_required
    def get(self, table_id):
        print(f'got a get to /table/{table_id}')
        current_user = models.User.objects(email=get_jwt_identity()).first()
        table = models.Table.objects(id=table_id, owner=current_user).first()
        if not table:
            return {}, 500
        return JSONEncoder().encode(table.to_client())

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

    @jwt_required
    def put(self, table_id):
        data = parser.parse_args()
        print(f'got a put to /table/{table_id} - {data}')
        current_user = models.User.objects(email=get_jwt_identity()).first()
        table = models.Table.objects(
            id=table_id, owner=current_user).first()
        if table:
            table.order = data['order']
            table.name = data['name']
            table.save()
            return JSONEncoder().encode(table.to_client())
        return {}, 500


class PostTable(Resource):
    @jwt_required
    def post(self):
        data = parser.parse_args()
        print(f'got a post to /table - {data}')
        current_user = models.User.objects(email=get_jwt_identity()).first()
        if current_user is not None:
            new_table = models.Table(
                name=data['name'], order=data['order'], owner=current_user)
            new_table.save()
            return new_table.to_json()
        else:
            return {}, 500


class Column(Resource):
    @jwt_required
    def post(self):
        data = parser.parse_args()
        print(f'got a post to /column - {data}')
        current_user = models.User.objects(email=get_jwt_identity()).first()
        table = models.Table.objects(
            owner=current_user, id=data['tableId']).first()
        if not table:
            return {}, 500
        column = models.Column(name=data['name'], table=table)
        column.save()
        return JSONEncoder().encode(column.to_client())

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
