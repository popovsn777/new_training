__author__ = 'popov.sn'

from model.member import Member

def test_update_first_record(app):
    app.session.login( username="admin", password="secret")
    app.new_member.edit_first_user(Member(firstname="Igo-go", lastname="Lub-bo", address="S.Peter-Peter",year = 2222))
###    self.return_to_home_page(wd)
    app.session.logout()