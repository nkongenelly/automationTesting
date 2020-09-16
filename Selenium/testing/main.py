import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from namasteFit.TestServer.Locators.locators import Locators
from selenium.webdriver.chrome.options import Options

# driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
# driver = webdriver.Chrome(executable_path=Locators.chrome_driver)
# driver.get("http://www.python.org")

# chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", Locators.mobile_emulation)
# chrome_options.add_argument(
#     '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=Locators.chrome_driver)
driver.get("http://www.python.org")

# Login email_field_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, email_field_id)))

assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
time.sleep(5)
elem.send_keys(Keys.RETURN)
time.sleep(5)
assert "No result found." not in driver.page_source
time.sleep(5)
driver.close()