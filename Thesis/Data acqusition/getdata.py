import requests
import cv2
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
link = 'https://fortune.com/ranking/fortune500/'

response = requests.get(link, headers=headers)
 
textbuffer = BeautifulSoup(response.text, 'html.parser') #Text we will receive

tag = "td"

dump = [] #List to 'dump' values into it
clean = [] #List for links

#Loop to find what's interesting for us in HTML buffer
for s in textbuffer.find_all('a'):
    print(s.get('href'))