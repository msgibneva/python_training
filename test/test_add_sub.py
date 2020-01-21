# -*- coding: utf-8 -*-
from model.subscriber import Subscriber


def test_add_sub(app, db, json_subscribers):
    subscriber = json_subscribers
    old_sub = db.get_sub_list()
    app.subscriber.create(subscriber)
    new_sub = db.get_sub_list()
    old_sub.append(subscriber)
    assert sorted(old_sub, key=Subscriber.id_or_max) == sorted(new_sub, key=Subscriber.id_or_max)

#def test_add_sub(app, json_subscribers):
#    subscriber = json_subscribers
#    old_sub = app.subscriber.get_sub_list()
#    app.subscriber.create(subscriber)
#    assert len(old_sub) + 1 == app.subscriber.count()
#    new_sub = app.subscriber.get_sub_list()
#    old_sub.append(subscriber)
#    assert sorted(old_sub, key=Subscriber.id_or_max) == sorted(new_sub, key=Subscriber.id_or_max)