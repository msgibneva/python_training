from selenium.webdriver.support.ui import Select

class SubscriberHelper:

    def __init__(self, app):
        self.app = app

    def create(self, subscriber):
        wd = self.app.wd
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
        self.return_to_home_page()

    def delete_first_subscriber(self):
        wd = self.app.wd
        #self.open_home_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()