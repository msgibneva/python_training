from model.subscriber import Subscriber


def test_edit_sub_name(app):
    old_sub = app.subscriber.get_sub_list()
    if app.subscriber.count() == 0:
        app.subscriber.create(Subscriber(firstname="subname"))
    app.subscriber.edit_first_sub(Subscriber(firstname="new"))
    new_sub = app.subscriber.get_sub_list()
    assert len(old_sub) == len(new_sub)

def test_edit_sub_nick(app):
    old_sub = app.subscriber.get_sub_list()
    if app.subscriber.count() == 0:
        app.subscriber.create(Subscriber(firstname="subname"))
    app.subscriber.edit_first_sub(Subscriber(nick="new"))
    new_sub = app.subscriber.get_sub_list()
    assert len(old_sub) == len(new_sub)