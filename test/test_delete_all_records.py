__author__ = 'popov.sn'

def test_delete_all_records(app):
    app.session.login( username="admin", password="secret")
    app.new_member.delete_all_records()
###    self.return_to_home_page(wd)
    app.session.logout()
