from pony.orm import *
from datetime import datetime
from model.group import Group
from model.subscriber import Subscriber
from pymysql.converters import decoders


class ORMFixture:

    db = Database()

    #набор классов для привязки. имя переменной = столбец бд
    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMSubscriber(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(str, column='deprecated')

    #выполняем привязку через конструктор
    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        #сопоставление полей таблиц
        self.db.generate_mapping()
        #показать sql запрос
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_subscribers_to_model(self, subscribers):
        def convert(subscriber):
            return Subscriber(id=str(subscriber.id), firstname=subscriber.firstname, lastname=subscriber.lastname)
        return list(map(convert, subscribers))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_sub_list(self):
        return self.convert_subscribers_to_model(select(c for c in ORMFixture.ORMSubscriber if c.deprecated is None))

