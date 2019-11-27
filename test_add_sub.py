# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class TestAddSub(unittest.TestCase):
    def setUp(self):
        self.wd= webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_sub(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_new_subscriber(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def create_new_subscriber(self, wd):
        # init subscriber creation
        wd.find_element_by_link_text("add new").click()
        # fill profile
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys("123")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys("dfgtg")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys("auidhls")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys("nic")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys("company")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys("address")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys("homephone")
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys("mobile")
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys("work")
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys("fax")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys("email1")
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys("email2")
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys("email3")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").send_keys("homesite")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("12")
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("December")
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys("1995")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("17")
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("November")
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys("2200")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys("addresssec")
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").send_keys("sechome")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").send_keys("notes")
        # submit new subscriber
        wd.find_element_by_name("submit").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
