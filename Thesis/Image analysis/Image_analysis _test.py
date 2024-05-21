
import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np
import os
import csv

reader = easyocr.Reader(['en'], gpu=True)
directory = r"C:\Users\Thomas\Documents\Thesis\Data acqusition\Screenshots"
csvfile = open('Image analysis/image_data.csv', 'w')
'''svwriter =csv.writer(csvfile)
csvwriter.writerow(['Company name', 'Image path', 'Has cookies', 'tl coord', 'br coord'])'''

'''for file in os.listdir(directory):
    path = os.path.join(directory, file)
    print(path.split('\\')[-1].split('.')[0].capitalize())'''

img = 'C:/Users/Thomas/Documents/Thesis/Data acqusition/Screenshots/3m.png'
result = reader.readtext(img)
for i in result:
    print(i[1].lower())
    if 'cookies' in i[1].lower() or 'cookie' in i[1].lower():
        print('cookie!')