from selenium.webdriver.support.ui import Select

class SubscriberHelper:

    def __init__(self, app):
        self.app = app

    def create(self, subscriber):
        wd = self.app.wd
        self.open_home_page()
        # init subscriber creation
        wd.find_element_by_link_text("add new").click()
        # fill profile
        self.fill_profile(subscriber)
        # submit new subscriber
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def edit_first_sub(self, new_subscriber_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_subscriber()
        # submit edition
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit profile
        self.fill_profile(new_subscriber_data)
        # submit edited subscriber
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()

    def fill_profile(self, subscriber):
        wd = self.app.wd
        self.change_field_value("firstname", subscriber.firstname)
        self.change_field_value("middlename", subscriber.secondname)
        self.change_field_value("lastname", subscriber.surname)
        self.change_field_value("nickname", subscriber.nick)
        self.change_field_value("title", subscriber.title)
        self.change_field_value("address", subscriber.homeaddress)
        self.change_field_value("company", subscriber.companyname)
        self.change_field_value("home", subscriber.homephone)
        self.change_field_value("mobile", subscriber.mobilephone)
        self.change_field_value("work", subscriber.work)
        self.change_field_value("fax", subscriber.faxnumber)
        self.change_field_value("email", subscriber.email1)
        self.change_field_value("email2", subscriber.email2)
        self.change_field_value("email3", subscriber.email3)
        self.change_field_value("homepage", subscriber.homesite)
        self.change_field_value("address2", subscriber.addresssec)
        self.change_field_value("phone2", subscriber.sechomenumber)
        self.change_field_value("notes", subscriber.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_subscriber(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_subscriber()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def select_first_subscriber(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")