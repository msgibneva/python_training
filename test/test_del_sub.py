from model.subscriber import Subscriber
import random
import allure


def test_delete_first_subscriber(app, db, check_ui):
    with allure.step('Given a subscribers list'):
        old_sub = db.get_sub_list()
        if len(db.get_sub_list()) == 0:
            app.subscriber.create(Subscriber(firstname="subname"))
        subscriber = random.choice(old_sub)
    with allure.step('When I delete the subscriber %s from the list' % subscriber):
        app.subscriber.delete_subscriber_by_id(subscriber.id)
    with allure.step('Then the new group list is equal to the old list without the deleted group'):
        assert len(old_sub) - 1 == app.subscriber.count()
        new_sub = db.get_sub_list()
        old_sub.remove(subscriber)
        assert old_sub == new_sub
        if check_ui:
            assert sorted(new_sub, key=Subscriber.id_or_max) == sorted(app.group.get_sub_list(),  key=Subscriber.id_or_max)