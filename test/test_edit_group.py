# -*- coding: utf-8 -*-
from model.group import Group
import random
import allure


def test_edit_group_name(app, db, check_ui):
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="firstgroup"))
        randgroup = random.choice(old_groups)
        group = Group(name="grname")
    with allure.step('When I edit a group %s in a list' % group):
        app.group.edit_group_by_id(group, randgroup.id)
    with allure.step('Then the new group list is equal to the old list with an edited group'):
        new_groups = db.get_group_list()
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),  key=Group.id_or_max)