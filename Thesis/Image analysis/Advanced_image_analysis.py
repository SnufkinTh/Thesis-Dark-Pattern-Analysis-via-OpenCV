
import easyocr
import os
import csv

reader = easyocr.Reader(['en', 'et'], gpu=True)                                 #Initialize easyocr text detection
directory = r"C:\Users\thoma\Documents\Thesis_new\Thesis\Data acqusition\Screenshots"     #Define screenshot folder location
csvfile = open('Image analysis/advanced_image_data_fortune_500_america.csv', 'w')
csvwriter =csv.writer(csvfile)
csvwriter.writerow(['Company name', 'Image path', 'Top-left coord', 'Bottom-Right coord', 'Cookies ?'])


for file in os.listdir(directory):
    print('Reading new image...')
    path = os.path.join(directory, file)
    result = reader.readtext(path)
    for i in result:
        if "cookie" in i[1].lower() or "cookies" in i[1].lower() or "küpsis" in i[1].lower() or "küpsised" in i[1].lower():
            cookies = True
            print(cookies)
            name = path.split('\\')[-1].split('.')[0].capitalize()                      #Extract company name from file name
            tl = tuple(i[0][0])                                                         #Extract top-left coordinate
            br = tuple(i[0][2])                                                         #Extract bottom right coordinate
            csvwriter.writerow([name, path, tl, br, cookies])                           #Save data to csv
            break
    else:                                                                               #What happens if no cookies found
        cookies = False
        print(cookies)
        name = path.split('\\')[-1].split('.')[0].capitalize()
        csvwriter.writerow([name, path, '-', '-', cookies])


            
    
    
