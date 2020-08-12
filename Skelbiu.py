import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options, executable_path='<pathto>/chromedriver.exe')

def renew():
    driver.get ('https://www.skelbiu.lt/users/renew')
    driver.find_element_by_id('nick').send_keys('login')
    driver.find_element_by_id('password').send_keys('password')
    driver.find_element_by_id('login-button').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="default_page_content"]/form/button').click()

renew()
