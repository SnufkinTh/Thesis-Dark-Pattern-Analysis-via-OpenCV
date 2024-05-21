from seleniumbase import Driver
from selenium.common.exceptions import WebDriverException, TimeoutException
import time
from selenium.webdriver.chrome.options import Options
import os
import csv


browser = Driver(headless=True, uc=True,)
browser.set_window_size(1920,1080)
browser.maximize_window()
file = open('Data acqusition/Data/links.txt', 'r')
csvfile = open('Data acqusition/Data/results.csv', 'w')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Company', 'Link', 'Status', 'Error'])


lines = file.readlines()
'''file1 = open('Data acqusition/Data/check.txt', 'a')
lines1 = file1.readlines()'''

for line in lines:
    name = line.split('.')[1]
    if os.path.isfile('Data acqusition/Screenshots/'+ name + '.png'):
        status = 'ok'
        csvwriter.writerow([name.capitalize(), line, status, '-'])
        print('ok')
    else:
        try:
            browser.set_page_load_timeout(12)
            browser.get(line)
            time.sleep(2) #vaja lidasa, muidu võib ruuter arvata, et DDOS rünnak ja peatab ühenduse + vaja oodata veidi, et leht laeks ära
            browser.save_screenshot("Data acqusition/Screenshots/"+ name + ".png")
            status = 'ok'
            csvwriter.writerow([name.capitalize(), line, status, '-'])
        except (WebDriverException, TimeoutException) as fault:
            status = 'error'
            if fault == WebDriverException:
                error = 'Connection Error'
            else:
                error = 'Timeout Error'
            csvwriter.writerow([name.capitalize(), line, status, error])
            print(error)
            pass

file.close()
