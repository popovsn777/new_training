__author__ = 'popov.sn'

from model.member import Member

def test_delete_first_record(app):

    app.new_member.delete_first_record()
###    self.return_to_home_page(wd)

