__author__ = 'popov.sn'
from model.group import Group



def test_midify_group_name(app):
    app.group.modify_first_group( Group(name="New group ppppp"))



def test_midify_group_header(app):
    app.group.modify_first_group( Group(header="New header rrrrrrrrrr"))
