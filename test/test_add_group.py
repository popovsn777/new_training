# -*- coding: utf-8 -*-
from model.group import Group



def test_(app):
    app.group.create( Group(name="group_name5", header="group_header5", footer="group_footer5"))

def test_(app):
    app.group.create( Group(name="New group AAA", header="group_header Alis", footer="group_footer Ali Baba"))


def test_add_empty_group(app):
    app.group.create( Group(name="", header="", footer=""))

