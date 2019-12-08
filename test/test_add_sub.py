# -*- coding: utf-8 -*-
from model.subscriber import Subscriber


def test_add_sub(app):
    app.subscriber.create(Subscriber(firstname ="123", secondname ="dfgtg", surname="auidhls", nick="nic", title="title", companyname="company", homeaddress="address", homephone="homephone",
                                     mobilephone="mobile", work="work", faxnumber="fax", email1="email1", email2="email2", email3="email3", homesite="homesite", addresssec="addresssec", sechomenumber="sechome", notes="notes"))

def test_add_empty_sub(app):
    app.subscriber.create(Subscriber(firstname ="", secondname ="", surname="", nick="", title="", companyname="", homeaddress="", homephone="",
                                     mobilephone="", work="", faxnumber="", email1="", email2="", email3="", homesite="", addresssec="", sechomenumber="", notes=""))