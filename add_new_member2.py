# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import  unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_new_member2(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_new_member2(self):
        wd = self.wd
        self.open_home_page(wd)
        #login
        self.login(wd, name="admin", password="secret")
        self.add_new_user(wd, firstname="Serg", lastname="Zat", address="Tula", year="1567")
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_new_member3(self):
        wd = self.wd
        self.open_home_page(wd)
        #login
        self.login(wd, name="admin", password="secret")
        self.add_new_user(wd, firstname="Igo", lastname="Lub", address="S.Peter", year="1111")
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_new_member4(self):
        wd = self.wd
        self.open_home_page(wd)
        #login
        self.login(wd, name="admin", password="secret")
        self.add_new_user(wd, firstname="Ludmila", lastname="Yakish", address="Kolomna", year="2000")
        self.return_to_home_page(wd)
        self.logout(wd)





    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def add_new_user(self, wd, firstname, lastname, address, year):
        # add new user
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[6]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(year)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd, name, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(name)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(name)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/addressbook/edit.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
