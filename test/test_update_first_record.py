__author__ = 'popov.sn'


def test_update_first_record(app):
    app.session.login( username="admin", password="secret")
    app.new_member.add_new_user(Member(firstname="Sergey", lastname="Zatula", address="Tula",year = 1788))
###    self.return_to_home_page(wd)
    app.session.logout()