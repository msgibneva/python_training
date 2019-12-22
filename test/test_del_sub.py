from model.subscriber import Subscriber


def test_delete_first_subscriber(app):
    old_sub = app.subscriber.get_sub_list()
    if app.subscriber.count() == 0:
        app.subscriber.create(Subscriber(firstname="subname"))
    app.subscriber.delete_first_subscriber()
    assert len(old_sub) - 1 == app.subscriber.count()
    new_sub = app.subscriber.get_sub_list()
    old_sub[0:1] = []
    assert old_sub == new_sub