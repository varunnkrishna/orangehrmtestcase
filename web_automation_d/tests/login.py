import sys
# sys.path.append('C:/Users/DELL/projects/web_automation/web_automation_d/pages')
from selenium import webdriver
import time
import unittest
# from homepage import HomePage
# from loginpage import LoginPage
from web_automation_d.pages.homepage import HomePage
from web_automation_d.pages.loginpage import LoginPage
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    # the setUpClass function will only run once
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/DELL/projects/web_automation/web_automation_d/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        #creating a variable 
        driver = self.driver

        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        homepage = HomePage(driver)
        homepage.welcome_click()
        homepage.logout_click()

        time.sleep(2)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/DELL/projects/web_automation/web_automation_d/reports'))
    #executing the file using python -m web_automation_d.tests.login command






