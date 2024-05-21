import cv2
import csv
from ast import literal_eval as make_tuple

data = open('C:/Users/Thomas/Documents/Thesis/Image analysis/image_data.csv', 'r')

reader = csv.reader(data)
next(reader) #skip header
print(next(reader))

def crop_image(name, path, tl_coord, br_coord):
    name = name
    path = path
    tl = tl_coord
    br = br_coord
    image = cv2.imread(path)
    print("Shape: ", image.shape)
    #Check cookie position

    #Check for lower part of banner
    if tl[1]>= 931:
        c_tl_x = 0
        c_tl_y = tl[1] - 150
        c_br_x = 1920
        c_br_y = 1080
    elif tl[1]<=149:
        if tl[0] > 150:
            c_tl_x = tl[0] - 150
        else:
            c_tl_x = 0
        c_tl_y = 0
        c_br_x = 1920
        c_br_y = br[1] + 150
    else:   
        if tl[0] > 150:
            c_tl_x = tl[0] - 150
        else:
            c_tl_x = 0
        if tl[1] > 150:
            c_tl_y = tl[1] - 150
        else:
            c_tl_y = 0
        if br[0] < 1770:
            c_br_x = br[0] + 150
        else:
            c_br_x = 1920
        if br[1] < 930:
            c_br_y = br[1] + 150  
        else:
            c_br_y = 1080
    crop = image[c_tl_y:c_br_y, c_tl_x:c_br_x]
    #cv2.imshow("Crop result", crop)
    cv2.imwrite('C:/Users/Thomas/Documents/Thesis/Image analysis/Analysed images/'+name+'.png', crop)
    return()


for line in reader:
    if line != []:
        name = line[0]
        image_path = line[1] #.replace('\\', '/')
        tl = make_tuple(line[2])
        br = make_tuple(line[3])
        print(tl[0])
        print(name)
        print(image_path)
        print(tl)
        print(br)
        crop_image(name, image_path, tl, br)

   
    

        


