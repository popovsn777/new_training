# -*- coding: utf-8 -*-
import pytest
from model.member import Member
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_member2(app):
    app.session.login( username="admin", password="secret")
    app.add_new_user(Member(firstname="Sergey", lastname="Zatula", address="Tula",year = 1788))

    self.return_to_home_page(wd)
    app.session.logout()

def test_add_new_member3(self):
    wd = self.wd
    self.open_home_page(wd)
    self.login(wd, name="admin", password="secret")
    self.add_new_user(wd, Member(firstname="Igo", lastname="Lub", address="S.Peter", year="1111"))
    self.return_to_home_page(wd)
    self.logout(wd)

def test_add_new_member4(self):
    wd = self.wd
    self.open_home_page(wd)
    self.login(wd, name="admin", password="secret")
    self.add_new_user(wd, Member(firstname="Ludmila", lastname="Yakish", address="Kolomna", year="2000"))
    self.return_to_home_page(wd)
    self.logout(wd)





    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        # return to home page
        wd.find_element_by_link_text("home page").click()

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
