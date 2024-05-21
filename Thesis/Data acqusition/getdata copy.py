import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

#Link passed to request
link = 'https://www.zyxware.com/articles/4344/list-of-fortune-500-companies-and-their-websites'


#File to write links into
file = open("Data acqusition/Data/links.txt", "w")



dump = [] #List to 'dump' values into it

response = requests.get(link, headers=headers)
print(response.text)
textbuffer = BeautifulSoup(response.text, 'html.parser') #Text we will receive
tag = "td"

#Loop to find what's interesting for us in HTML buffer
for table in textbuffer.find_all('table', class_="table"):
    for tr in table.find_all('tr'):
        td = tr.find_all('td')
        for text in td:
            reg_str = "<" + tag + ">(.*)</" + tag + ">"
            res = re.findall(reg_str, str(text))
            dump.append(res[0])

#Loop to extract from dump
for hlink in (dump):
    if hlink[:4] == "http":
        file.write(hlink + '\n')
file.close()