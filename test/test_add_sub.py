# -*- coding: utf-8 -*-
from model.subscriber import Subscriber
import allure



def test_add_sub(app, db, json_subscribers, check_ui):
    subscriber = json_subscribers
    with allure.step('Given a subscribers list'):
        old_sub = db.get_sub_list()
    with allure.step('When I add a subscriber %s to the list' % subscriber):
        app.subscriber.create(subscriber)
    with allure.step('Then the new subscribers list is equal to the old list with the added subscriber'):
        new_sub = db.get_sub_list()
        old_sub.append(subscriber)
        assert sorted(old_sub, key=Subscriber.id_or_max) == sorted(new_sub, key=Subscriber.id_or_max)
        if check_ui:
            assert sorted(new_sub, key=Subscriber.id_or_max) == sorted(app.subscriber.get_sub_list(), key=Subscriber.id_or_max)