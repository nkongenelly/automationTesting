import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from namasteFit.TestServer.Locators.locators import Locators
from namasteFit.CommonFiles.blazeMeterCrossBrowser import BlazeMeterCrossBrowserSignin
from namasteFit.TestServer.Pages.loginPage import LoginPage
from namasteFit.CommonFiles.blazeArgs import BlazeArgs
from namasteFit.TestServer.Locators.credentials import Credentials
blazemeterTest = BlazeMeterCrossBrowserSignin()
driver = blazemeterTest.ChromeTests()

# open url
# fill search filed
blazeArgs = BlazeArgs()
blazeArgs.blazemeterArgsStart(driver, "'namaste.fit connect with google test'", "Accessing " + Locators.testServer)
try:
   driver.get(Locators.testServer)
   blazeArgs.addArgs('passed', '')
except AssertionError as exc:
   blazeArgs.addArgs('failed', '')
except BaseException as exc:
   blazeArgs.addArgs('broken', '')
blazeArgs.blazemeterArgsStop()



#Get email and password
email = input("Enter email: ")
password = input('Input password: ')
time.sleep(4)

assert "Instructor:Namaste.fit" in driver.title
#login
loginPage = LoginPage(driver)
driverOptions = "chrome"
loginPage.login(driver, driverOptions, email, password)
print(loginPage)


# # check title
# assert "Python" in driver.title
#
# # fill search filed
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
#
# # check is search not empty
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()