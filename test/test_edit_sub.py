from model.subscriber import Subscriber


def test_edit_sub_name(app):
    app.subscriber.edit_first_sub(Subscriber(firstname="new"))

def test_edit_sub_nick(app):
    app.subscriber.edit_first_sub(Subscriber(nick="new"))