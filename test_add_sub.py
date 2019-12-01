# -*- coding: utf-8 -*-
import pytest
from subscriber import Subscriber
from subapplication import Subapplication

@pytest.fixture
def app(request):
    fixture = Subapplication()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_sub(app):
    app.login(username = "admin", password = "secret")
    app.create_new_subscriber(Subscriber(name = "123", secondname = "dfgtg", surname="auidhls", nick="nic", title="title", companyname="company", homeaddress="address", homephone="homephone",
                                   mobilephone="mobile", work="work", faxnumber="fax", email1="email1", email2="email2", email3="email3", homesite="homesite", bday="12", bmonth="December",
                                   aday="17", amonth="November", byear="1995", ayear="2200", addresssec="addresssec", sechomenumber="sechome", notes="notes"))
    app.logout()

def test_add_empty_sub(app):
    app.login(username = "admin", password = "secret")
    app.create_new_subscriber(Subscriber(name = "", secondname = "", surname="", nick="", title="", companyname="", homeaddress="", homephone="",
                                   mobilephone="", work="", faxnumber="", email1="", email2="", email3="", homesite="", bday="-", bmonth="-",
                                   aday="-", amonth="-", byear="", ayear="", addresssec="", sechomenumber="", notes=""))
    app.logout()