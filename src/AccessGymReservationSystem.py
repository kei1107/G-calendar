from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options

import time
import os
import sys


def access(mdid, pw, activity_location, logger):
    main_url = 'http://133.6.82.138/undou/mudy0010c.php'

    options = Options()
    options.binary_location = None
    if os.name == 'posix':
        options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    elif os.name == 'nt':
        options.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'

    if options.binary_location is None:
        logger.info('Support : Windows , OSX')
        sys.exit()
    try:
        options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=options)

        # http://133.6.82.138/undou/mudy0010c.php
        driver.get(main_url)
        logger.info('Accessing <http://133.6.82.138/undou/mudy0010c.php>')
        logger.info('Try login')

        try_cnt = 0
        while True:
            try_cnt += 1
            time.sleep(2)  # rendering
            login_id = driver.find_element_by_id('txtMdId')

            if login_id is None:
                if try_cnt >= 10:
                    logger.info('Access failure. Please check web site state.')
                    sys.exit()
                continue

            login_pw = driver.find_element_by_id('txtPw')
            login_button = driver.find_element_by_id('button')
            login_id.send_keys(mdid)
            login_pw.send_keys(pw)
            login_button.click()
            break

        # http://133.6.82.138/undou/mudy0020c.php
        try_cnt = 0
        while True:
            try_cnt += 1
            time.sleep(2)  # rendering
            login_button2s = driver.find_elements_by_id('button2')
            if (login_button2s is None) or (len(login_button2s) == 0):
                if try_cnt >= 15:
                    logger.info('Access failure. Please retry or check mdid , pw in settings.ini .')
                    sys.exit()
                continue

            logger.info('Access success')
            logger.info('loading gym reservation')
            login_button2s[int(activity_location)].click()
            break

        time.sleep(1)
        try:
            Alert(driver).accept()
        except:
            pass

        # http://133.6.82.138/undou/mudy0020c.php
        try_cnt = 0
        while True:
            try_cnt += 1
            time.sleep(2)  # rendering

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            detail = soup.find(id='detail')
            if detail is None:
                if try_cnt >= 15:
                    logger.info('Access failure. Please retry.')
                    sys.exit()
                continue

            with open('scraping-data/index' + activity_location + '.html', mode='w', encoding='utf-8') as fw:
                fw.write(soup.prettify())
            driver.quit()
            logger.info('Success data scraping.')
            break
    except Exception as e:
        logger.info('Error occured!')
        logger.exception(e)
        sys.exit()
