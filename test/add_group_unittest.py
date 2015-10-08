# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_(app):
    app.login( username="admin", password="secret")
    app.create_group( Group(name="group_name5", header="group_header5", footer="group_footer5"))
    app.logout()

def test_add_empty_group(app):
    app.login( username="admin", password="secret")
    app.create_group( Group(name="", header="", footer=""))
    app.logout()
