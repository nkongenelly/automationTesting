import sys
import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from namasteFit.TestServer.Locators.locators import Locators
from namasteFit.TestServer.Locators.accounts import Accounts
from namasteFit.TestServer.Pages.loginPage import LoginPage

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

# Site customize
class Google(unittest.TestCase):
    def setUp(self):
        # desired_capabilities['chromeOptions'] = {
        #     "args": ["--disable-extensions"],
        #     "extensions": []
        # }
        # self.options = webdriver.ChromeOptions().add_argument("--user-data-dir=" + Locators.chrome_user_profile)
        self.options = webdriver.ChromeOptions().add_argument(['--disable-web-security', '--user-data-dir' + Locators.chrome_user_profile, '--allow-running-insecure-content'])

        args: ['--disable-web-security', '--user-data-dir', '--allow-running-insecure-content']

        self.driver = webdriver.Chrome(chrome_options=self.options, executable_path=Locators.chrome_driver)
        self.driver.get(Locators.testServer)
        return self.driver


    def test_login(self):
        driver = self.driver
        time.sleep(2)

        # Navigate to Login Page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.connect_with_google_xpath)))
        driver.find_element_by_xpath(Locators.connect_with_google_xpath).click()

        # Define variables
        email = Accounts.email
        password = Accounts.password

        # Enter email and click next
        loginPage = LoginPage(driver)
        loginPage.enterEmail(email)
        loginPage.enterEmailNext()

        # Enter password and click next
        loginPage.enterPassword(password)
        loginPage.enterPasswordNext()

        time.sleep(1)

        # Assertain successful login logo exists
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.successful_login_logo_xpath)))
        namasteLogo = driver.find_elements(By.TAG_NAME, 'img')

        for image in namasteLogo:
            current_link = image.get_attribute("src")
            print("current_link")
            assert current_link == "/static/media/logo.e1ae6d8b.png"
            print(current_link)
            self.assertEqual("/static/media/logo.e1ae6d8b.png", current_link)


    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main_':
    unittest.main()