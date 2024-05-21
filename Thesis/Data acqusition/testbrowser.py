
from selenium.common.exceptions import WebDriverException, TimeoutException
import time
from selenium.webdriver.chrome.options import Options
import os
import csv
import undetected_chromedriver as uc

browser = uc.Chrome()
browser.set_window_size(1920,1080)
browser.maximize_window()

browser.get('https://www.iqvia.com/')

browser.save_screenshot("Data acqusition/Screenshots/test.png")
