# -*- coding: utf-8 -*-
from model.subscriber import Subscriber
import pytest
from data.add_sub import constant as testdata


@pytest.mark.parametrize("subscriber", testdata, ids=[repr(x) for x in testdata])
def test_add_sub(app, subscriber):
    old_sub = app.subscriber.get_sub_list()
    app.subscriber.create(subscriber)
    assert len(old_sub) + 1 == app.subscriber.count()
    new_sub = app.subscriber.get_sub_list()
    old_sub.append(subscriber)
    assert sorted(old_sub, key=Subscriber.id_or_max) == sorted(new_sub, key=Subscriber.id_or_max)