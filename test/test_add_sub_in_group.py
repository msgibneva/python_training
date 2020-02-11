import random
from fixture.orm import ORMFixture
from model.group import Group
from model.subscriber import Subscriber
import allure


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_subscriber_to_group(app):
    if len(db.get_sub_list()) == 0:
        app.contact.create(Subscriber(firstname="firstname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="firstgroup"))
    with allure.step('Given a group list'):
        group_list = db.get_group_list()
    with allure.step('Given a subscribers list'):
        sub_list = db.get_sub_list()
        old_sub_list = db.get_sub_in_groups()
        subscriber = None

        for g in group_list:
            list_subs_not_in_group = db.get_sub_not_in_group(g)
            if list_subs_not_in_group:
                subscriber = random.choice(list_subs_not_in_group)
                app.subscriber.add_sub_to_group(subscriber, g)
                break
        if subscriber is None:
            header = 'test'
            app.group.create(Group(header=header))
            group = db.get_group_by_header(header)
            subscriber = random.choice(sub_list)
    with allure.step('When I add a subscriber to the group %s' % group):
        app.subscriber.add_sub_to_group(subscriber, group)
    with allure.step('Then the new subscribers list in group is equal to the old list with an added subscriber'):
        subs = db.get_sub_in_groups()
        if len(subs) + 1 == len(old_sub_list):
            return True
