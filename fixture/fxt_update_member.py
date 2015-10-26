__author__ = 'popov.sn'
from fixture.new_member import MemberHelper

class UpdateHelper ():


    def update_user(self):
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Igo-go")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Lub-bo")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("S.Peter-Peter")
        if not wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[8]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[4]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2222")
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

