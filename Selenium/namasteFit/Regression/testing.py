class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value

    def add(self, key, value):
        self[key] = value

landingPages = my_dictionary()
landingPages['pages'] = {["home"],["/home/studio"], ["/home/get-started"]}
landingPages['status'] = {["passed", "failed", "broken"]}
landingPages['messages'] = {"YOU HAVE NO ACCESS TO THE STUDIO PLATFORM","PLEASE PUBLISH YOUR STUDIO FIRST", "WELCOME BACK TO YOUR STUDIO PLATFORM"}

for a,i in landingPages:
    print(landingPages[a])

# import getpass
# import sys
# import os
# import timeit
# import unittest
# import time
# from filecmp import cmp
#
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver import DesiredCapabilities
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# # from ..TestServer.Locators.locators import Locators
# # from ..TestServer.Pages.loginPage import LoginPage
# from namasteFit.TestServer.Locators.locators import Locators
# from namasteFit.CommonFiles.crossBrowserSignin import CrossBrowserSignin
# from namasteFit.TestServer.Locators.accounts import Accounts
# from namasteFit.TestServer.Pages.loginPage import LoginPage
#
# sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
# # unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: cmp(y, x)
#
# class my_dictionary(dict):
#
#     # __init__ function
#     def __init__(self):
#         self = dict()
#
#         # Function to add key:value
#
#     def add(self, key, value):
#         self[key] = value
#
#     # Main Function
#
#
# # dict_obj = my_dictionary()
#
# class Testing(unittest.TestCase):
#     def setUp(self):
#         print('Enter the gmailid and password')
#         # self.email, self.password = map(str, input().split())
#         self.email = input("Enter email: ")
#         self.password = input('Input password: ')
#         # self.password = getpass.getpass('Input password: ')
#         self.ChromeTests()
#         # self.firefoxTests()
#
#     def EdgeTests(self):
#         self.driver = webdriver.Edge(executable_path=Locators.microsoft_edge_driver)
#         self.driver.get(Locators.testServer)
#         self.driver.maximize_window()
#
#         return self.driver
#
#     def ChromeTests(self):
#         self.options = webdriver.ChromeOptions()
#         self.options.add_extension(extension=Locators.chrome_extension)
#
#         mobile_emulation = {"deviceName": "Nexus 5"}
#
#         # chrome_options = webdriver.ChromeOptions()
#
#         self.options.add_experimental_option("mobileEmulation", mobile_emulation)
#
#         # driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
#         #
#         #                           desired_capabilities=chrome_options.to_capabilities())
#
#         # self.options.add_argument(['--disable-web-security', '--user-data-dir' + Locators.chrome_user_self.options, '--allow-running-insecure-content'])
#         self.options.add_argument("--no-sandbox")
#         self.options.add_argument("--disable-save-passsword-bubble")
#         self.options.add_argument('--user-data-dir' + Locators.chrome_user_profile)
#         self.options.add_argument('--disable-web-security')
#         self.options.add_argument('disable-infobars')
#         self.options.add_argument('--allow-running-insecure-content')
#         self.options.add_experimental_option("useAutomationExtension", False)
#         # self.options .setExperimentalOption("excludeSwitches", Collections.singletonList("enable-automatiion"))
#         desired = DesiredCapabilities.CHROME
#
#         prefs = {
#             "credentials_enable_service": False,
#             "profile.password_manager_enabled": False
#         }
#
#         self.options.add_experimental_option('prefs', prefs)
#         self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
#         self.driver = webdriver.Chrome(options=self.options, executable_path=Locators.chrome_driver)
#
#         self.driver.get(Locators.testServer)
#         self.driver.maximize_window()
#
#         # self.login(self.driver)
#
#         return self.driver
#
#     def firefoxTests(self):
#         # self.driver = webdriver.Firefox(executable_path=Locators.firefox_driver)
#         # # driver = webdriver.Firefox()
#         # self.driver.get(Locators.testServer)
#         # self.driver.maximize_window()
#         # time.sleep(10)
#
#         self.options = webdriver.FirefoxOptions()
#         self.options.add_argument('--user-data-dir' + Locators.firefox_user_profile)
#         # PROXY_HOST = "12.12.12.123"
#         # PROXY_PORT = "1234"
#         self.options.set_preference("network.proxy.type", 1)
#         # self.options.set_preference("network.proxy.http", PROXY_HOST)
#         # self.options.set_preference("network.proxy.http_port", int(PROXY_PORT))
#         self.options.set_preference("dom.webdriver.enabled", False)
#         self.options.set_preference('useAutomationExtension', False)
#         # self.options.update_preference()
#         # self.options.update_preferences()
#         desired = DesiredCapabilities.FIREFOX
#
#         # self.driver = webdriver.Firefox(firefox_profile=self.options, desired_capabilities=desired, executable_path=Locators.firefox_driver)
#         self.driver = webdriver.Firefox(options=self.options, desired_capabilities=desired,
#                                         executable_path=Locators.firefox_driver)
#         # self.driver = webdriver.Firefox(options=self.options, executable_path=Locators.firefox_driver)
#
#         self.driver.set_page_load_timeout(20)
#         self.driver.get(Locators.testServer)
#         while True:
#             try:
#                 # self.driver.get(Locators.testServer)
#                 self.driver.maximize_window()
#             except TimeoutException:
#                 print
#                 "Timeout, retrying..."
#                 continue
#             else:
#                 break
#
#         return self.driver
#
#     def test_login(self):
#         driver = self.driver
#         time.sleep(2)
#         # Define variables
#         email = self.email
#         password = self.password
#         # print('Enter the gmailid and password')
#         # email, password = map(str, input().split())
#
#         # email = Accounts.email
#         # password = Accounts.password
#
#         try:
#             # Navigate to Login Page
#             WebDriverWait(driver, 30).until(
#                 EC.presence_of_element_located((By.XPATH, Locators.connect_with_google_xpath)))
#             driver.find_element_by_xpath(Locators.connect_with_google_xpath).click()
#
#             # Enter email and click next
#             loginPage = LoginPage(driver)
#             loginPage.enterEmail(email)
#             loginPage.enterEmailNext()
#             time.sleep(3)
#
#             # Enter password and click next
#             loginPage.enterPassword(password)
#             loginPage.enterPasswordNext()
#             start = timeit.timeit()
#             end = timeit.timeit()
#
#             time.sleep(10)
#             self.landingPage(end, start, driver)
#
#         except:
#             print('Login Failed')
#
#     def landingPage(self, end, start, driver):
#         # driver = self.driver
#         # get URl after successful login
#         loginURL = driver.current_url
#         print("Time taken to sign in is : ")
#         print(end - start)
#         print("current URl = ")
#         print(loginURL)
#
#         if loginURL == Locators.testServer:
#             print("YOU HAVE NO ACCESS TO THE STUDIO PLATFORM")
#
#         elif loginURL == Locators.testServer + "/home/studio":
#             print("PLEASE PUBLISH YOUR STUDIO FIRST")
#
#         driver.close()
#         time.sleep(5)
#         # self.firefoxTests()
#
#         # Assertain successful login logo exists
#         # WebDriverWait(self.driver, 10).until(
#         #     EC.presence_of_element_located((By.XPATH, Locators.successful_login_logo_xpath)))
#         # namasteLogo = driver.find_elements(By.TAG_NAME, 'img')
#         #
#         # for image in namasteLogo:
#         #     current_link = image.get_attribute("src")
#         #     print("current_link")
#         #     assert current_link == "/static/media/logo.e1ae6d8b.png"
#         #     print(current_link)
#         #     self.assertEqual("/static/media/logo.e1ae6d8b.png", current_link)
#
#     # def tearDown(self) -> None:
#     #     self.driver.close()
#
#
# if __name__ == '__main_':
#     unittest.main()