from tabla_server import db


class User(db.Document):
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)


class Table(db.Document):
    name = db.StringField(required=True)
    order = db.IntField()
    owner = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)

    def header_to_client(self):
        son = self.to_mongo()
        son['id'] = str(son['_id'])
        son.pop('_id', None)
        son.pop('owner', None)
        return son

    def to_client(self):
        son = self.to_mongo()
        son['id'] = str(son['_id'])
        son['columns'] = []
        son.pop('_id', None)
        son.pop('owner', None)
        columns = Column.objects(table=self)
        for column in columns:
            son['columns'].append(column.to_client())
        return son


class Column(db.Document):
    name = db.StringField(required=True)
    order = db.IntField()
    table = db.ReferenceField(Table, reverse_delete_rule=db.CASCADE)
    owner = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)

    def to_client(self):
        son = self.to_mongo()
        son['id'] = str(son['_id'])
        son['entries'] = []
        son.pop('_id', None)
        son.pop('owner', None)
        son.pop('table', None)
        entries = Entry.objects(column=self)
        for entry in entries:
            son['entries'].append(entry.to_client())
        return son


class Entry(db.Document):
    name = db.StringField()
    order = db.IntField()
    column = db.ReferenceField(Column, reverse_delete_rule=db.CASCADE)
    owner = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)

    def to_client(self):
        son = self.to_mongo()
        son['id'] = str(son['_id'])
        son.pop('_id', None)
        son.pop('owner', None)
        son.pop('column', None)
        return son
