from tabla_server import db


class User(db.Document):
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)


class Table(db.Document):
    title = db.StringField(required=True)
    owner = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)


class Column(db.Document):
    title = db.StringField(required=True)
    table = db.ReferenceField(Table, reverse_delete_rule=db.CASCADE)
    position = db.IntField()


class Entry(db.Document):
    title = db.StringField(required=True)
    text = db.StringField()
    position = db.IntField()
    column = db.ReferenceField(Column, reverse_delete_rule=db.CASCADE)
