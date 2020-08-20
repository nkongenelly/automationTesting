from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import unittest
#import HTMLTestRunner
from namasteFit.TestServer.Locators.locators import Locators


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=Locators.firefox_driver)
        self.driver.get(Locators.testServer + Locators.login_url)
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.set_script_timeout(60)
        namaste_username = "nelly@namaste.fit"
        namaste_password = "qwertyui"

        email_field_id = "form-signin-email"
        pass_field_id = "form-signin-password"
        login_button_xpath = "//*[@id='formLogin']/button"
        namaste_logo_xpath = "//*[@id='mainLogo']"

        email_field_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, email_field_id)))
        pass_field_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, pass_field_id)))
        login_button_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_button_xpath)))

        email_field_element.clear()
        email_field_element.send_keys(namaste_username)

        pass_field_element.clear()
        pass_field_element.send_keys(namaste_password)

        login_button_element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, namaste_logo_xpath)))

    # def tear_down(self):
    #     self.driver.close()


if __name__ == '__main__':
    unittest.main()


