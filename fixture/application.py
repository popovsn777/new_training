from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.new_member import MemberHelper
__author__ = 'Elmira'

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.new_member = MemberHelper(self)
        self

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/")

    def destroy(self):
        self.wd.quit()