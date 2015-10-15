# -*- coding: utf-8 -*-
from model.member import Member


def test_add_new_member2(app):
    app.session.login( username="admin", password="secret")
    app.new_member.add_new_user(Member(firstname="Sergey", lastname="Zatula", address="Tula",year = 1788))
###    self.return_to_home_page(wd)
    app.session.logout()

def test_add_new_member3(app):
    app.session.login( username="admin", password="secret")
    app.new_member.add_new_user( Member(firstname="Igo", lastname="Lub", address="S.Peter", year="1111"))
###    self.return_to_home_page(wd)
    app.session.logout()

def test_add_new_member4(app):
    app.session.login( username="admin", password="secret")
    app.new_member.add_new_user( Member(firstname="Ludmila", lastname="Yakish", address="Kolomna", year="2000"))
###    self.return_to_home_page(wd)
    app.session.logout()



"""
    def return_to_home_page(self, wd):
        # return to home page
        wd.find_element_by_link_text("home page").click()

"""

