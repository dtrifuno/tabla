from tabla_server import db


class User(db.Document):
    email = db.StringField(required=True, unique=True, max_length=50)
    password = db.StringField(required=True)


class Table(db.Document):
    name = db.StringField(required=True, max_length=150)
    prev = db.ReferenceField('self', required=False)
    owner = db.ReferenceField(
        User, required=True, reverse_delete_rule=db.CASCADE)

    def header_to_client(self):
        son = self.to_mongo()
        son['id'] = str(son['_id'])
        if son.get('prev', None) is not None:
            son['prev'] = str(son['prev'])
        else:
            son['prev'] = None
        son.pop('_id', None)
        son.pop('owner', None)
        return son

    def to_client(self):
        son = self.to_mongo()
        son['id'] = str(son['_id'])
        if son.get('prev', None) is not None:
            son['prev'] = str(son['prev'])
        else:
            son['prev'] = None
        son['columns'] = []
        son.pop('_id', None)
        son.pop('owner', None)
        columns = Column.objects(table=self)
        for column in columns:
            son['columns'].append(column.to_client())
        return son


class Column(db.Document):
    name = db.StringField(required=True)
    prev = db.ReferenceField('self', required=False)
    table = db.ReferenceField(Table, reverse_delete_rule=db.CASCADE)
    owner = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)

    def to_client(self):
        son = self.to_mongo()
        son['id'] = str(son['_id'])
        son.pop('_id', None)
        if son.get('prev', None) is not None:
            son['prev'] = str(son['prev'])
        else:
            son['prev'] = None
        son['entries'] = []
        son.pop('owner', None)
        son.pop('table', None)
        entries = Entry.objects(column=self)
        for entry in entries:
            son['entries'].append(entry.to_client())
        return son


class Entry(db.Document):
    name = db.StringField()
    prev = db.ReferenceField('self', required=False)
    column = db.ReferenceField(Column, reverse_delete_rule=db.CASCADE)
    owner = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)

    def to_client(self):
        son = self.to_mongo()
        son['id'] = str(son['_id'])
        son.pop('_id', None)
        if son.get('prev', None) is not None:
            son['prev'] = str(son['prev'])
        else:
            son['prev'] = None
        son.pop('owner', None)
        son.pop('column', None)
        return son
