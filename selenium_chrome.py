from selenium import webdriver
import time

options = webdriver.ChromeOptions() ;
prefs = {"download.default_directory" : "D:\src\small-projects-python"}; # path where the file will be saved
options.add_experimental_option("prefs",prefs);

# driver path to GoogleChrome control, each browser has its own driver, you can also add it to your OS environment variables
driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe',chrome_options=options);

try:
    driver.get('https://www.browserstack.com/test-on-the-right-mobile-devices'); # sample website for file download

    downloadcsv= driver.find_element_by_css_selector('.icon-csv');
    gotit= driver.find_element_by_id('accept-cookie-notification');

    gotit.click();    
    downloadcsv.click();
    
    time.sleep(5)
    driver.close()
except:
     print("Invalid URL")