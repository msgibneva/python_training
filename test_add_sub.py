# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from subscriber import Subscriber

class TestAddSub(unittest.TestCase):
    def setUp(self):
        self.wd= webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_sub(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username = "admin", password = "secret")
        self.create_new_subscriber(wd, Subscriber(name = "123", secondname = "dfgtg", surname="auidhls", nick="nic", title="title", companyname="company", homeaddress="address", homephone="homephone",
                                   mobilephone="mobile", work="work", faxnumber="fax", email1="email1", email2="email2", email3="email3", homesite="homesite", bday="12", bmonth="December",
                                   aday="17", amonth="November", byear="1995", ayear="2200", addresssec="addresssec", sechomenumber="sechome", notes="notes"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_sub(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username = "admin", password = "secret")
        self.create_new_subscriber(wd, Subscriber(name = "", secondname = "", surname="", nick="", title="", companyname="", homeaddress="", homephone="",
                                   mobilephone="", work="", faxnumber="", email1="", email2="", email3="", homesite="", bday="-", bmonth="-",
                                   aday="-", amonth="-", byear="", ayear="", addresssec="", sechomenumber="", notes=""))
        self.return_to_home_page(wd)
        self.logout(wd)

    def create_new_subscriber(self, wd, subscriber):
        # init subscriber creation
        wd.find_element_by_link_text("add new").click()
        # fill profile
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(subscriber.name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(subscriber.secondname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys(subscriber.surname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys(subscriber.nick)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys(subscriber.title)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys(subscriber.companyname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys(subscriber.homeaddress)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(subscriber.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys(subscriber.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys(subscriber.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys(subscriber.faxnumber)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(subscriber.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys(subscriber.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys(subscriber.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").send_keys(subscriber.homesite)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(subscriber.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(subscriber.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(subscriber.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(subscriber.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(subscriber.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys(subscriber.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys(subscriber.addresssec)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").send_keys(subscriber.sechomenumber)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").send_keys(subscriber.notes)
        # submit new subscriber
        wd.find_element_by_name("submit").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
