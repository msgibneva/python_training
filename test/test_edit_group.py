# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="grname"))
    app.group.edit_first_group(Group(name="new"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="grname"))
    app.group.edit_first_group(Group(header="new"))