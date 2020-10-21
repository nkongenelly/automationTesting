import getpass
import sys
import os
import unittest
from namasteFit.CommonFiles.crossBrowserSignin import CrossBrowserSignin
from namasteFit.TestServer.Pages.loginPage import LoginPage


sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
# unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: cmp(y, x)

class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value

    def add(self, key, value):
        self[key] = value

    # Main Function


# dict_obj = my_dictionary()

class Google(unittest.TestCase):
    def setUp(self):
        # self.email, self.password = map(str, input().split())
        self.email = input("Enter email: ")
        self.password = input('Input password: ')
        # self.password = getpass.getpass('Input password: ')
        # self.ChromeTests()
        # self.firefoxTests()
        crossbrowser = CrossBrowserSignin()
        # crossbrowser = BlazeMeterCrossBrowserSignin()
        chrome_driver = crossbrowser.ChromeTests()
        chrome_mobile_driver_nexus = crossbrowser.ChromeMobileTestsNexus()
        chrome_mobile_driver_galaxy = crossbrowser.ChromeMobileTestsGalaxy()
        firefox_driver = crossbrowser.firefoxTests()
        edge_driver = crossbrowser.EdgeTests()
        self.drivers = my_dictionary()
        self.drivers['chrome'] = chrome_driver
        self.drivers['chromeMobileNexus'] = chrome_mobile_driver_nexus
        self.drivers['chromeMobileGalaxy'] = chrome_mobile_driver_galaxy
        self.drivers['firefox'] = firefox_driver
        self.drivers['edge'] = edge_driver

        print("ALL DRIVERS = ")
        for driver in self.drivers.values():
            print(driver)
        return self.drivers
        drivers.append(firefox_driver)


    def test_login(self):
        for driverOptions in self.drivers:

            # time.sleep(10)
            print("again")
            print(driverOptions)
            self.driver = self.drivers[driverOptions]
            driver = self.driver
            # webbrowser.open('https://'+ 'a.blazemeter.com' +'/api/v4/grid/sessions/' + self.driver.session_id + '/redirect/to/report')

            loginPage = LoginPage(driver)
            loginPage.login(driver, driverOptions, self.email, self.password)
            print(loginPage)





    # def tearDown(self) -> None:
    #     self.driver.close()

if __name__ == '__main_':
    unittest.main()