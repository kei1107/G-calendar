from bs4 import BeautifulSoup
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options

import time
import os
import sys


def Access(Mdid, Pw):
    main_url = 'http://133.6.82.138/undou/mudy0010c.php'

    options = Options()
    options.binary_location = None
    if os.name == 'posix':
        options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
    elif os.name == 'nt': \
            options.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'

    if options.binary_location is None:
        print('What\'s your OS ??? ')
        sys.exit()

    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)

    # http://133.6.82.138/undou/mudy0010c.php
    driver.get(main_url)
    print('Accessing')
    time.sleep(2)  # rendering
    print('Try login')
    login_id = driver.find_element_by_id('txtMdId')
    login_pw = driver.find_element_by_id('txtPw')
    login_button = driver.find_element_by_id('button')
    login_id.send_keys(Mdid)
    login_pw.send_keys(Pw)
    login_button.click()

    # http://133.6.82.138/undou/mudy0020c.php
    time.sleep(10)  # rendering
    login_button2s = driver.find_elements_by_id('button2')
    if len(login_button2s) == 0:
        print('Access failure. Please retry.')
        sys.exit()
    print('Access success')
    print('loading gym reservation')
    login_button2s[-1].click()

    time.sleep(1)
    Alert(driver).accept()

    # http://133.6.82.138/undou/mudy0020c.php
    time.sleep(5)  # rendering

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
    driver.save_screenshot('ss.png')
    driver.quit()
