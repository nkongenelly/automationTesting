import unittest
# import HTMLTestRunner
from namasteFit.TestServer.Locators.locators import Locators
import namasteFit.CommonFiles.login as LoginValid
# global driver


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = LoginValid.login_set_up(Locators.firefox_driver, Locators.testServer, Locators.login_url)

    def test_login(self):
        driver = self.driver
        LoginValid.test_login(driver)


if __name__ == '__main__':
    unittest.main()
