
import easyocr
import os
import csv

reader = easyocr.Reader(['en', 'et'], gpu=True)                             #Initialize easyocr text detection
directory = r"C:\Users\Thomas\Documents\Thesis\Data acqusition\Screenshots" #Define screenshot folder location
csvfile = open('Image analysis/image_data.csv', 'w')
csvwriter =csv.writer(csvfile)
csvwriter.writerow(['Company name', 'Image path', 'Top-left coord', 'Bottom-Right coord'])


for file in os.listdir(directory):
    print('Starting to read data...')
    path = os.path.join(directory, file)                            #Image path is combined from folder path + image name
    result = reader.readtext(path)
    for i in result:
        if "cookie" in i[1].lower() or "cookies" in i[1].lower() or "küpsis" in i[1].lower() or "küpsised" in i[1].lower():
            name = path.split('\\')[-1].split('.')[0].capitalize()  #Extract company name from file name
            tl = tuple(i[0][0])
            br = tuple(i[0][2])                                     #Extract bottom right coordinate
            csvwriter.writerow([name, path, tl, br])                 #Save data to csv
            break


            
    
    
