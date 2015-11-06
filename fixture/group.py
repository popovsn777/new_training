__author__ = 'Elmira'

from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        print("DEBUG open_group_page1")
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        print("DEBUG open_group_page 2")

    def create(self, group):
        print("create 3")
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        print("create 4")
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_css_selector("#content > form").click()
        wd.find_element_by_name("submit").click()
        self.return_to_group()
        print("create 5")

    def fill_group_form(self, group):
        print("fill_group_form 7")
        # fill group form
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        print("fill_group_form 8")
        self.change_field_value("group_header", group.header)
        print("fill_group_form 9")
        self.change_field_value("group_footer", group.footer)
        print("fill_group_form 10")



    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group()

    def select_first_group(self):
        # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form( new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()


    def return_to_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_element_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_group_page()
        groups = []
        for element in wd.find_element_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get.attribute("value")
            groups.append(Group(name=text, id=id))
        return groups

