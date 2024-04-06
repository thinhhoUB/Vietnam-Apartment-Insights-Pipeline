from seleniumbase import Driver
from time import sleep
from seleniumbase import Driver
from bs4 import BeautifulSoup
from datetime import datetime
from sys import path
import secrets
import logging

page_url= 'https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-tp-hcm'

def createChromeDriver(num_chrome):
    chrome_drivers = []
    for _ in range(num_chrome):
        driver = Driver(uc_cdp=True, incognito=True,block_images=True,headless=True)
        chrome_drivers.append(driver)
    return chrome_drivers

print(createChromeDriver(5))