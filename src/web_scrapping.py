from seleniumbase import Driver
from time import sleep
from seleniumbase import Driver
from bs4 import BeautifulSoup
from datetime import datetime
from sys import path
import secrets
import logging
import re

page_url= 'https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-tp-hcm'

#create multiple Chrome WebDriver instances.
def createChromeDriver(num_chrome):
    chrome_drivers = []
    for _ in range(num_chrome):
        driver = Driver(uc_cdp=True, incognito=True,block_images=True,headless=True)
        chrome_drivers.append(driver)
    return chrome_drivers

#getting URLs for each listing in single page
def extract_property_urls_single_page(page_url,html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    base_url= page_url
    property_urls=[base_url+element.get('href') for element in soup.select('.js__product-link-for-product-id')]
    return property_urls

#coordinates extraction
def extract_coordinates(html_content):
    # Define a regular expression pattern to extract coordinates
    pattern = r'place\?q=([-+]?\d*\.\d+),([-+]?\d*\.\d+)'

    # Use re.search to find the first match in the HTML content
    match = re.search(pattern, html_content)

    # Check if a match is found
    if match:
        # Extract latitude and longitude from the matched groups
        latitude = float(match.group(1))
        longitude = float(match.group(2))
        return [latitude, longitude]
    else:
        return [None,None]
    
    