__author__ = 'popov.sn'

from model.member import Member

def test_delete_first_record(app):

    app.new_member.delete_first_record()

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
###    self.return_to_home_page(wd)

