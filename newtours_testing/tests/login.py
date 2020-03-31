from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time
from pages import Registration_page

class Registration_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('test case for registration')
        cls.driver = webdriver.Chrome(executable_path="C:/Users/DELL/projects/web_automation/newtours_testing/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        

    def test_001_registerClass(self):
        #creating a variable
        driver = self.driver
        driver.get('http://newtours.demoaut.com/')
        driver.find_element_by_link_text('REGISTER').click()
        reg_test = Registration_page(driver)
        reg_test.enter_fname('krishna')
        reg_test.enter_lname('varun')
        reg_test.enter_phone('8332881993')
        reg_test.enter_uname('90.varunkrishna@gmail.com')
        reg_test.enter_address1('newyork apartments newyork')
        reg_test.enter_address2('tarnaka')
        reg_test.enter_city('hyderabad')
        reg_test.enter_state('telangana')
        reg_test.enter_postalcode('500017')
        reg_test.enter_country('india')
        reg_test.enter_email('py.varunkrishna@gmail.com')
        reg_test.enter_password('drive123')
        reg_test.enter_r_password('drive123')
        reg_test.click_register()

        time.sleep(10)
    
    def test_002_login(self):
        driver = self.driver
        driver.get('http://newtours.demoaut.com/')
        driver.find_element_by_name('userName').send_keys('py.varunkrishna@gmail.com')
        driver.find_element_by_name('password').send_keys('drive123')
        driver.find_element_by_name('login').click()
        print('login sucessful')
        signoff = driver.find_elements_by_partial_link_text('SIGN-OFF')
        signoff[0].click()
        time.sleep(5)
        print('signoff sucessful')


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('test completed for login')

if __name__== "__main__":
    unittest.main()