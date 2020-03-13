import unittest
import sys
from selenium import webdriver
class TestLogin(unittest.TestCase):
    phone = "15218884975"
    password = "a1234567"
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baokaodaxue.com/")
        self.driver.find_element_by_class_name('use_btn').click()
    def test_login(self):
        self.driver.find_element_by_class_name('login_btn').click()
        self.driver.find_element_by_class_name('phone').send_keys(self.phone)
        self.driver.find_element_by_class_name('pwd').send_keys(self.password)
        self.driver.find_element_by_class_name('submit_btn').click()
        print("登陆")
    def test_login2(self):
        # self.driver.quit()
        print("sss")
if __name__ == '__main__':
    unittest.main()

















