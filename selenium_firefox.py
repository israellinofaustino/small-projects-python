from selenium import webdriver
import time

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "D:\src\small-projects-python")
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

driver = webdriver.Firefox(firefox_profile = profile, executable_path=r'C:\geckodriver\geckodriver.exe')

try:
    driver.get('https://www.browserstack.com/test-on-the-right-mobile-devices');

    gotit= driver.find_element_by_id('accept-cookie-notification');
    gotit.click();

    downloadcsv = driver.find_element_by_css_selector('.icon-csv');
    downloadcsv.click();

    time.sleep(5)
    driver.quit();
except:
    print ("Invalid URL")