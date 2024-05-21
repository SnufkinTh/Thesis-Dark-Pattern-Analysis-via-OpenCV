from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.chrome.options import Options
import os
import csv

custom_options = Options()                           #Call options class to overwrite
custom_options.add_argument("--headless")            #No display mode
custom_options.add_argument('window-size=1920,1080') #Screen size
custom_options.add_argument("start-maximized")       #Full-screen
browser = webdriver.Chrome(options=custom_options)   #Launch browser with custom options

file = open('Data acqusition/Data/new_links.txt', 'r')
csvfile = open('Data acqusition/Data/results.csv', 'w')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Company', 'Link', 'Status', 'Error'])


lines = file.readlines()
'''file1 = open('Data acqusition/Data/check.txt', 'a')
lines1 = file1.readlines()'''

for line in lines:
    name = line.split('.')[1]                                           #Extract company name from link
    if os.path.isfile('Data acqusition/Screenshots/'+ name + '.png'):   #Check if .png file with similar name exists
        status = 'ok'
        csvwriter.writerow([name.capitalize(), line, status, '-'])      #If exists save into .CSV file result
        print('ok')
    else:
        try:
            browser.set_page_load_timeout(20)                                      #Set Timeout Error timer.
            browser.get(line)                                                      #Go to link
            browser.save_screenshot("Data acqusition/Screenshots/"+ name + ".png") #Save screenshot
            status = 'ok'
            csvwriter.writerow([name.capitalize(), line, status, '-'])
        except (WebDriverException, TimeoutException) as fault:                    #Catch exceptions
            status = 'error'
            if fault is WebDriverException:
                error = 'Connection Error'
            else:
                error = 'Timeout Error'
            csvwriter.writerow([name.capitalize(), line, status, error])
            print(error)
            pass

file.close()
