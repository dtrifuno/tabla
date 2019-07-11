from tabla_server import db


class User(db.Document):
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)


class Table(db.Document):
    name = db.StringField(required=True)
    order = db.IntField()
    owner = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)


class Column(db.Document):
    name = db.StringField(required=True)
    order = db.IntField()
    table = db.ReferenceField(Table, reverse_delete_rule=db.CASCADE)
    owner = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)


class Entry(db.Document):
    name = db.StringField()
    order = db.IntField()
    column = db.ReferenceField(Column, reverse_delete_rule=db.CASCADE)
    owner = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)
