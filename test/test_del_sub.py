from model.subscriber import Subscriber

def test_delete_first_subscriber(app):
    if app.subscriber.count() == 0:
        app.subscriber.create(Subscriber(firstname="subname"))
    app.subscriber.delete_first_subscriber()