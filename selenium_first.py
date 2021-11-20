from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe');
driver.get("http://www.python.org")
assert "Python" in driver.title # confirm that title has “Python” word in it
elem = driver.find_element_by_name("q") # Finding HTML Element
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close() # close the browser