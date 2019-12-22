from model.subscriber import Subscriber


def test_edit_sub_name(app):
    old_sub = app.subscriber.get_sub_list()
    subscriber = Subscriber(firstname="new")
    subscriber.id = old_sub[0].id
    if app.subscriber.count() == 0:
        app.subscriber.create(Subscriber(firstname="name"))
    app.subscriber.edit_first_sub(subscriber)
    assert len(old_sub) == app.subscriber.count()
    new_sub = app.subscriber.get_sub_list()
    old_sub[0] = subscriber
    assert sorted(old_sub, key=Subscriber.id_or_max) == sorted(new_sub, key=Subscriber.id_or_max)

def test_edit_sub_lastname(app):
    old_sub = app.subscriber.get_sub_list()
    subscriber = Subscriber(firstname="new", lastname="new")
    subscriber.id = old_sub[0].id
    if app.subscriber.count() == 0:
        app.subscriber.create(Subscriber(firstname="name"))
    app.subscriber.edit_first_sub(subscriber)
    assert len(old_sub) == app.subscriber.count()
    new_sub = app.subscriber.get_sub_list()
    old_sub[0] = subscriber
    assert sorted(old_sub, key=Subscriber.id_or_max) == sorted(new_sub, key=Subscriber.id_or_max)