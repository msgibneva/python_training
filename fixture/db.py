import pymysql.cursors
from model.group import Group
from model.subscriber import Subscriber

class DbFixture():

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        #autocommit clears cache db
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_sub_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, mobile, email, email2, email3, home, work, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, mobile, email, email2, email3, home, work, phone2) = row
                list.append(Subscriber(id=str(id), firstname=firstname, lastname=lastname, homeaddress=address, mobilephone=mobile,
                                       email1=email, email2=email2, email3=email3, homephone=home, work=work, sechomenumber=phone2))
        finally:
            cursor.close()
        return list

    def get_sub_in_group(self, group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, group_id from address_in_groups where group_id=?", str(group_id))
            row = cursor.fetchone()
            list.append(row)
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
