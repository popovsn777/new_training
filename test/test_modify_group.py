__author__ = 'popov.sn'
from model.group import Group



def test_midify_group_name(app):
    app.group.modify( Group(name="New group", header="group_header5", footer="group_footer5"))



def test_midify_group_name(app):
    app.group.modify( Group(name="New group", header="group_header5", footer="group_footer5"))

