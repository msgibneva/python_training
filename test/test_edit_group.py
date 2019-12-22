# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(group)
    index = randrange(len(old_groups))
    group = Group(name="grname")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_edit_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(group)
#    index = randrange(len(old_groups))
#    group = Group(header="grheader")
#    group.id = old_groups[index].id
#    app.group.edit_group_by_index(group, index)
#    assert len(old_groups) == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups[index] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)