from pony.orm import *
from datetime import datetime
from model.group import Group
from model.subscriber import Subscriber
from pymysql.converters import decoders, conversions


class ORMFixture:

    db = Database()

    #набор классов для привязки. имя переменной = столбец бд
    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        subscribers = Set(lambda: ORMFixture.ORMSubscriber, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMSubscriber(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        last_name = Optional(str, column='lastname')
        deprecated = Optional(str, column='deprecated', sql_default=None)
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='subscribers', lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_subscribers_to_model(self, subscribers):
        def convert(subscriber):
            return Subscriber(id=str(subscriber.id), firstname=subscriber.first_name, lastname=subscriber.last_name)
        return list(map(convert, subscribers))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_group_by_header(self, header):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup if g.header == header))[0]

    @db_session
    def get_sub_list(self):
        return self.convert_subscribers_to_model(select(c for c in ORMFixture.ORMSubscriber if c.deprecated is None))

    @db_session
    def get_sub_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_subscribers_to_model(orm_group.subscribers)

    @db_session
    def get_sub_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_subscribers_to_model(select(c for c in ORMFixture.ORMSubscriber if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_sub_in_groups(self):
        orm_sub = list(select(g for g in ORMFixture.ORMSubscriber if g.groups))
        return self.convert_subscribers_to_model(orm_sub)
