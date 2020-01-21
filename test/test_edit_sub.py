from model.subscriber import Subscriber
import random


def test_edit_sub_name(app, db, check_ui):
    old_sub = db.get_sub_list()
    if len(db.get_sub_list()) == 0:
        app.subscriber.create(Subscriber(firstname="name"))
    randsubscriber = random.choice(old_sub)
    subscriber = Subscriber(firstname="new")
    app.subscriber.edit_sub_by_id(subscriber, randsubscriber.id)
    new_sub = db.get_sub_list()
    assert old_sub == new_sub
    if check_ui:
        assert sorted(new_sub, key=Subscriber.id_or_max) == sorted(app.subscriber.get_sub_list(), key=Subscriber.id_or_max)

#def test_edit_sub_name(app):
#    old_sub = app.subscriber.get_sub_list()
#    if app.subscriber.count() == 0:
#        app.subscriber.create(Subscriber(firstname="name"))
#    index = randrange(len(old_sub))
#    subscriber = Subscriber(firstname="new")
#    subscriber.id = old_sub[index].id
#    app.subscriber.edit_sub_by_index(subscriber, index)
#    assert len(old_sub) == app.subscriber.count()
#    new_sub = app.subscriber.get_sub_list()
#    old_sub[index] = subscriber
#    assert sorted(old_sub, key=Subscriber.id_or_max) == sorted(new_sub, key=Subscriber.id_or_max)

#def test_edit_sub_lastname(app):
#    old_sub = app.subscriber.get_sub_list()
#    subscriber = Subscriber(firstname="new", lastname="new")
#    subscriber.id = old_sub[0].id
#    if app.subscriber.count() == 0:
#        app.subscriber.create(Subscriber(firstname="name"))
#    app.subscriber.edit_first_sub(subscriber)
#    assert len(old_sub) == app.subscriber.count()
#    new_sub = app.subscriber.get_sub_list()
#    old_sub[0] = subscriber
#    assert sorted(old_sub, key=Subscriber.id_or_max) == sorted(new_sub, key=Subscriber.id_or_max)