# -*- coding: utf-8 -*-
from model.group import Group



def test_(app):
    app.session.login( username="admin", password="secret")
    app.group.create( Group(name="group_name5", header="group_header5", footer="group_footer5"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login( username="admin", password="secret")
    app.group.create( Group(name="", header="", footer=""))
    app.session.logout()
