from model.subscriber import Subscriber
import random

def test_delete_first_subscriber(app, db):
    old_sub = db.get_sub_list()
    if len(db.get_sub_list()) == 0:
        app.subscriber.create(Subscriber(firstname="subname"))
    subscriber = random.choice(old_sub)
    app.subscriber.delete_subscriber_by_id(subscriber.id)
    assert len(old_sub) - 1 == app.subscriber.count()
    new_sub = db.get_sub_list()
    old_sub.remove(subscriber)
    assert old_sub == new_sub

#def test_delete_first_subscriber(app):
#    old_sub = app.subscriber.get_sub_list()
#    if app.subscriber.count() == 0:
#        app.subscriber.create(Subscriber(firstname="subname"))
#    index = randrange(len(old_sub))
#    app.subscriber.delete_subscriber_by_index(index)
#    assert len(old_sub) - 1 == app.subscriber.count()
#    new_sub = app.subscriber.get_sub_list()
#    old_sub[index:index + 1] = []
#    assert old_sub == new_sub