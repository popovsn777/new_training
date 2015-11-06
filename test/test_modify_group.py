__author__ = 'popov.sn'
from model.group import Group



def test_midify_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group( Group(name="New group ppppp"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_midify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group( Group(header="New header rrrrrrrrrr"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
