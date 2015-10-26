__author__ = 'popov.sn'

import pytest
from model.group import Group
from fixture.application import Application


def test_delete_first_group(app):
    app.group.delete_first_group()
