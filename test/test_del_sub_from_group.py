# from fixture.orm import ORMFixture
# from model.subscriber import Subscriber
# from model.group import Group
# import random
#
# db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
#
# def test_del_sub_from_group(app):
#     if len(db.get_sub_list()) == 0:
#         app.subscriber.create(Subscriber(firstname="firstname"))
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="groupname"))
#     if len(db.get_sub_in_groups()) == 0:
#         group = random.choice(app.group.get_group_list())
#         subscriber = random.choice(app.subscriber.get_sub_list())
#         app.subscriber.add_sub_to_group(subscriber, group)
#     group_list = app.group.get_group_list()
#     old_subs_from_group = db.get_clients_from_group(group)
#     app.subscriber.delete_sub_from_group_by_id(subscriber, group)
#     new_subs_from_group = db.get_sub_from_group(group)
#     assert len(old_clients_from_group) == len(new_clients_from_group) - 1


    # for g in group_list:
    #     list_sub_in_group = db.get_sub_in_group(g)
    #     if list_sub_in_group:
    #         subscriber = random.choice(list_sub_in_group)
    #         app.subscriber.delete_sub_from_group_by_id(subscriber, g)
    #         sub_list = db.get_sub_in_group(g)
    #         assert subscriber not in sub_list
    #         break