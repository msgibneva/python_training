from model.subscriber import Subscriber


def test_edit_sub_name(app):
    if app.subscriber.count() == 0:
        app.subscriber.create(Subscriber(firstname="subname"))
    app.subscriber.edit_first_sub(Subscriber(firstname="new"))

def test_edit_sub_nick(app):
    if app.subscriber.count() == 0:
        app.subscriber.create(Subscriber(firstname="subname"))
    app.subscriber.edit_first_sub(Subscriber(nick="new"))