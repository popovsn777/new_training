# -*- coding: utf-8 -*-
from model.group import Group



def test_(app):
    old_groups = app.group.get_group_list()
    app.group.create( Group(name="group_name5", header="group_header5", footer="group_footer5"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_(app):
    old_groups = app.group.get_group_list()
    app.group.create( Group(name="New group AAA", header="group_header Alis", footer="group_footer Ali Baba"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    app.group.create( Group(name="", header="", footer=""))

