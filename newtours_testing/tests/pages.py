class Registration_page():

    def __init__(self, driver):
        self.driver = driver

        #regitration page: locators
        self.fname_textbox_name = 'firstName'
        self.lname_textbox_name = 'lastName'
        self.phone_textbox_pnum = 'phone'

        self.username_textbox_xpath = "//input[@name='userName']"
        self.address1_textbox_name = "address1"
        self.address2_textbox_name = "address2"
        self.city_textbox_name = "city"
        self.state_textbox_name = "state"
        self.postalcode_textbox_name = "postalCode"
        self.country_textbox_name = "country"

        self.email_textbox_name = "email"
        self.password_textbox_name = "password"
        self.cpassword__textbox_name = "confirmPassword"
        self.register_submitbutton = "register"

    def enter_fname(self, fname):
        # self.driver.find_element_by_name(self.fname_textbox_name).clear()
        self.driver.find_element_by_name(self.fname_textbox_name).send_keys(fname)
    
    def enter_lname(self, lname):
        # self.driver.find_element_by_name(self.lname_textbox_name).clear()
        self.driver.find_element_by_name(self.lname_textbox_name).send_keys(lname)

    def enter_phone(self, pno):
        # self.driver.find_element_by_name(self.phone_textbox_pnum).clear()
        self.driver.find_element_by_name(self.phone_textbox_pnum).send_keys(pno)

    def enter_uname(self, uname):
        # self.driver.find_elements_by_xpath(self.username_textbox_xpath).clear()
        username = self.driver.find_elements_by_xpath(self.username_textbox_xpath)
        username[0].send_keys(uname)

    def enter_address1(self, add1):
        address1 = self.driver.find_elements_by_name(self.address1_textbox_name)
        address1[0].send_keys(add1)

    def enter_address2(self, add2):
        address2 = self.driver.find_elements_by_name(self.address2_textbox_name)
        address2[0].send_keys(add2)

    def enter_city(self, city):
        city_name = self.driver.find_elements_by_name(self.city_textbox_name)
        return city_name[0].send_keys(city)

    def enter_state(self, state):
        state_name = self.driver.find_elements_by_name(self.state_textbox_name)
        state_name[0].send_keys(state)

    def enter_postalcode(self, pcode):
        postalcode = self.driver.find_elements_by_name(self.postalcode_textbox_name)
        postalcode[0].send_keys(pcode)
    
    def enter_country(self, country):
        country_name = self.driver.find_elements_by_name(self.country_textbox_name)
        country_name[0].send_keys(country)
    
    def enter_email(self, email):
        self.driver.find_element_by_name(self.email_textbox_name).clear()
        self.driver.find_element_by_name(self.email_textbox_name).send_keys(email)
    
    def enter_password(self, pwd):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(pwd)
    
    def enter_r_password(self, rpwd):
        self.driver.find_element_by_name(self.cpassword__textbox_name).clear()
        self.driver.find_element_by_name(self.cpassword__textbox_name).send_keys(rpwd)
    
    def click_register(self):
        register = self.driver.find_elements_by_name(self.register_submitbutton)
        register[0].click()