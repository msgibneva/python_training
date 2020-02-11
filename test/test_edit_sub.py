from model.subscriber import Subscriber
import random
import allure


def test_edit_sub_name(app, db, check_ui):
    with allure.step('Given a subscribers list'):
        old_sub = db.get_sub_list()
        if len(db.get_sub_list()) == 0:
            app.subscriber.create(Subscriber(firstname="name"))
        randsubscriber = random.choice(old_sub)
        subscriber = Subscriber(firstname="new")
    with allure.step('When I edit a subscriber %s in the list' % subscriber):
        app.subscriber.edit_sub_by_id(subscriber, randsubscriber.id)
    with allure.step('Then the new subscribers list is equal to the old list with an edited subscriber'):
        new_sub = db.get_sub_list()
        assert old_sub == new_sub
        if check_ui:
            assert sorted(new_sub, key=Subscriber.id_or_max) == sorted(app.subscriber.get_sub_list(), key=Subscriber.id_or_max)