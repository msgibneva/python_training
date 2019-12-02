# -*- coding: utf-8 -*-
import pytest
from model.subscriber import Subscriber
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_sub(app):
    app.session.login(username = "admin", password = "secret")
    app.subscriber.create(Subscriber(name ="123", secondname ="dfgtg", surname="auidhls", nick="nic", title="title", companyname="company", homeaddress="address", homephone="homephone",
                                     mobilephone="mobile", work="work", faxnumber="fax", email1="email1", email2="email2", email3="email3", homesite="homesite", bday="12", bmonth="December",
                                     aday="17", amonth="November", byear="1995", ayear="2200", addresssec="addresssec", sechomenumber="sechome", notes="notes"))
    app.session.logout()

def test_add_empty_sub(app):
    app.session.login(username = "admin", password = "secret")
    app.subscriber.create(Subscriber(name ="", secondname ="", surname="", nick="", title="", companyname="", homeaddress="", homephone="",
                                     mobilephone="", work="", faxnumber="", email1="", email2="", email3="", homesite="", bday="-", bmonth="-",
                                     aday="-", amonth="-", byear="", ayear="", addresssec="", sechomenumber="", notes=""))
    app.session.logout()