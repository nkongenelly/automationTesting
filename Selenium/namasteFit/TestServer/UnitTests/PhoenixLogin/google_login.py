import unittest
# import HTMLTestRunner
import namasteFit.CommonFiles.login as LoginValid
from namasteFit.TestServer.Locators.locators import Locators
from selenium import webdriver
# global driver


class LoginTest(unittest.TestCase):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.proxy_type', 1)
        profile.set_preference('network.proxy.http', "127.0.0.1")
        profile.set_preference('network.proxy.http_port', "8090")
        profile.update_preferences()
        self.driver = webdriver.Firefox(firefox_profile=profile, executable_path=Locators.firefox_driver)
        # self.driver = LoginValid.login_set_up(Locators.firefox_driver, Locators.testServer, Locators.login_url)

    def test_login(self):
        driver = self.driver
        # driver = webdriver.Firefox(self.driver)
        driver.get(Locators.testServer + Locators.login_url)
        LoginValid.test_login(driver)

    def test_security(self):
        zap = "zap"

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
