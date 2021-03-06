__author__ = 'Elmira'

class MemberHelper:

    def __init__(self, app):
        self.app = app


    def add_new_user(self, member):
        # add new user
        wd = self.app.wd

        wd.find_element_by_link_text("add new").click()

        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(member.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(member.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(member.address)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[6]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(member.year)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def edit_first_user(self, member):

        wd = self.app.wd

        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(member.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(member.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(member.address)
        if not wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[8]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[4]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(member.year)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()


    def delete_first_record(self):
        wd = self.app.wd
        self.select_first_address()
        wd.find_element_by_css_selector("form[name='MainForm'] input[value='Delete']").click()

    def select_first_address(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@name='MainForm']/table[@id='maintable']//input[@name='selected[]']").click()


    def delete_all_records(self):
        wd = self.app.wd


#        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        wd.find_element_by_link_text("home").click()
        if not wd.find_element_by_id("MassCB").is_selected():
            wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.find_element_by_xpath("//div/div[3]/ul/li[1]/a").click()