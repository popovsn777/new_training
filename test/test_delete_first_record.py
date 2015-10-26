__author__ = 'popov.sn'

from model.member import Member

def test_update_first_record(app):
    app.session.login( username="admin", password="secret")
    app.new_member.delete_first_record()
###    self.return_to_home_page(wd)
    app.session.logout()
