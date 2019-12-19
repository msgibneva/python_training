# -*- coding: utf-8 -*-
from model.subscriber import Subscriber


def test_add_sub(app):
    old_sub = app.subscriber.get_sub_list()
    app.subscriber.create(Subscriber(firstname ="123", secondname ="dfgtg", surname="auidhls", nick="nic", title="title", companyname="company", homeaddress="address", homephone="homephone",
                                     mobilephone="mobile", work="work", faxnumber="fax", email1="email1", email2="email2", email3="email3", homesite="homesite", addresssec="addresssec", sechomenumber="sechome", notes="notes"))
    new_sub = app.subscriber.get_sub_list()
    assert len(old_sub) + 1 == len(new_sub)

def test_add_empty_sub(app):
    old_sub = app.subscriber.get_sub_list()
    app.subscriber.create(Subscriber(firstname ="", secondname ="", surname="", nick="", title="", companyname="", homeaddress="", homephone="",
                                     mobilephone="", work="", faxnumber="", email1="", email2="", email3="", homesite="", addresssec="", sechomenumber="", notes=""))
    new_sub = app.subscriber.get_sub_list()
    assert len(old_sub) + 1 == len(new_sub)