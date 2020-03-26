# from locators import Locators
from web_automation_d.locators_file.locators import Locators

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        #defining the locators of homepage
        self.welcome_button_id = Locators.welcome_button_id
        self.logout_link_linktext = Locators.logout_link_linktext

    def welcome_click(self):
        self.driver.find_element_by_id(self.welcome_button_id).click()

    def logout_click(self):
        self.driver.find_element_by_link_text(self.logout_link_linktext).click()