#! /usr/bin/python3
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import sys

username = sys.argv[1]
password = sys.argv[2]

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options, executable_path='/usr/lib/chromium-browser/chromedriver')

def renew():
    driver.get ('https://www.skelbiu.lt/users/renew')
    driver.find_element_by_id('nick').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    login_button = driver.find_element_by_xpath('//*[@id="login-button"]')
    driver.execute_script("arguments[0].click();", login_button)
    driver.implicitly_wait(1)
    renew_button = driver.find_element_by_xpath('//*[@id="default_page_content"]/form/button')
    driver.execute_script("arguments[0].click();", renew_button)

renew()
