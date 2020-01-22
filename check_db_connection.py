import pymysql.cursors
from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    subscribers = db.get_sub_list()
    for subscriber in subscribers:
        print(subscriber)
    print(len(subscribers))
finally:
    db.destroy()