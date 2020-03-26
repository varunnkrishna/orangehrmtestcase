from web_automation_d.locators_file.locators import Locators


class LoginPage():
    #creating a constructer
    def __init__(self, driver):
        self.driver = driver

        #defining the locators of loginpage
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
    

    #creating functions
    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()
    
    def click_invalid_msg(self):
        msg = self.driver.find_elements_by_css_selector(self.invalid_msg).text
        return msg


