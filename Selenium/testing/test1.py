from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from namasteFit.TestServer.Locators.locators import Locators
import time
import unittest
# import HTMLTestRunner


class LoginTest(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
        self.driver = webdriver.Safari(executable_path=Locators.chrome_driver)
        self.driver.get("http://app.raawmove.com/login")
        self.driver.maximize_window()

        # chrome_options = Options()
        # chrome_options.add_argument(
        #     '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
        # driver = webdriver.Chrome(options=chrome_options)
        # driver.get('https://www.google.com')

    def test_login(self):
        driver = self.driver
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

    def tear_down(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()


