__author__ = 'popov.sn'


from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.new_member import MemberHelper



class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)

        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.new_member = MemberHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/")
#        wd.get("http://localhost/addressbook/")



    def destroy(self):
        self.wd.quit()