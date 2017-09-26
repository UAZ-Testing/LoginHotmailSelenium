# coding=utf-8

import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://login.live.com/')

    def tearDown(self):
        pass
        #self.driver.close()

    def test_login(self):
        tbox_email = self.driver.find_element_by_name('loginfmt')
        tbox_email.send_keys('porfirioads@hotmail.com')
        tbox_email.send_keys(Keys.RETURN)

        tbox_pass = self.driver.find_element_by_name('passwd')
        tbox_pass.send_keys('password')
        tbox_pass.send_keys(Keys.RETURN)

        time.sleep(3)

        btn_login = self.driver.find_element_by_id('idSIButton9')
        btn_login.click()


# Ejecuta las pruebas implementadas
if __name__ == '__main__':
    unittest.main()
