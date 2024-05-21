import cv2
import os
import csv
import easyocr
from math import sqrt
from colorthief import ColorThief
from datetime import datetime

now = datetime.now().strftime('%H%M%S')
counter = 0
reader = easyocr.Reader(['en', 'et'], gpu=True)
image_folder = r'C:\Users\thoma\Documents\Thesis_new\Thesis\Data acqusition\Screenshots'
cascade = cv2.CascadeClassifier('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/training_result/cascade.xml')

csvfile = open('image analysis/solution_data_'+now+'.csv', 'w')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Name', 'Image-path', 'Result', 'Pattern list'])
centers = []

def union(a,b):
    x = min(a[0], b[0])
    y = min(a[1], b[1])
    w = max(a[0]+(a[2] +50), b[0]+b[2]) - x
    h = max(a[1]+a[3], b[1]+b[3]) - y
    return [x, y, w, h]

def _intersect(a,b):
    x = max(a[0], b[0])
    y = max(a[1], b[1])
    w = min(a[0]+a[2], b[0]+b[2]) - x
    h = min(a[1]+a[3], b[1]+b[3]) - y
    if h<0:
        return False
    return True

def _group_rectangles(rec):

    tested = [False for i in range(len(rec))]
    final = []
    i = 0
    while i < len(rec):
        if not tested[i]:
            j = i+1
            while j < len(rec):
                if not tested[j] and _intersect(rec[i], rec[j]):
                    rec[i] = union(rec[i], rec[j])
                    tested[j] = True
                    j = i
                j += 1
            final += [rec[i]]
        i += 1

    return final


def save_to_file(name, path, result, pattern_list):
    name = name
    path = path
    result = result
    pattern_list = pattern_list
    csvwriter.writerow([name, path, result, pattern_list])
    return

def find_cookies(list, image, counter):
    counter = counter
    rectangles = list
    image = image
    image = cv2.imread(image)
    width_img = image.shape[0] #Vahetame kohad ära, sest OpenCV loeb pilti külili
    height_img = image.shape[1]
    # print(width_img, height_img)
    max_area = 175000
    for (x, y , w, h) in rectangles:
        # print(x, y, w ,h)
        area = round(w * h)
        if area <= max_area:
            multiplier = sqrt(max_area/ area) #Meil vaja saada telgede jaoks kordajat, seega vaja võta ruutjuur pindala kordajast
            diff_w = round((w * multiplier - w)/ 2) #Pikkuse erinevus esialgsest --- peavad olema täisarvud
            diff_h = round((h * multiplier - h)/ 2) #Laiuse erinevus esialgsest
            # print(diff_w, diff_h)
            if x - diff_w >=0 and (y - diff_h) >= 0 and (x + diff_w) <= width_img and (y + diff_h) <= height_img:
                tl_x = x - diff_w
                br_x = x + w + diff_w
                tl_y = y - diff_h
                br_y = y + h + diff_h
            elif x - diff_w >=0 and x + diff_w <= width_img and y + diff_h <= height_img:
                tl_x = x + w - diff_w
                br_x = x + w + diff_w
                tl_y = y 
                br_y = y + h + diff_h
            elif x - diff_w >=0 and x + diff_w <= width_img and y - diff_h >= 0:
                tl_x = x + w - diff_w
                br_x = x + w + diff_w
                tl_y = y - diff_h
                br_y = y + h
            elif y - diff_h >= 0 and y + diff_h <= height_img and x + diff_w <= width_img:
                tl_x = x 
                br_x = x + w + diff_w
                tl_y = y - diff_h
                br_y = y + h + diff_h
            elif y - diff_h >= 0 and y + diff_h <= height_img and x - diff_w >= 0:
                tl_x = x - diff_w
                br_x = x + w
                tl_y = y - diff_h
                br_y = y + h + diff_h          
            elif x - diff_w >=0 and x + diff_w <= width_img:
                tl_x = x + w - diff_w
                br_x = x + w + diff_w
                tl_y = y 
                br_y = y + h
            elif y - diff_h >= 0 and y + diff_h <= height_img:
                tl_x = x 
                br_x = x + w
                tl_y = y - diff_h
                br_y = y + h + diff_h
            elif x - diff_w >= 0 and y - diff_h >= 0:
                tl_x = x - diff_w
                br_x = x + w
                tl_y = y - diff_h
                br_y = y + h
            elif x + diff_w <= width_img and y + diff_h <= height_img:
                tl_x = x
                br_x = x + w + diff_w
                tl_y = y
                br_y = y + h + diff_h
            elif x + diff_w <= width_img and y - diff_h >= 0:
                tl_x = x - diff_w
                br_x = x + w + diff_w
                tl_y = y - diff_h
                br_y = y + h
            elif y + diff_h <= height_img and x - diff_w >= 0:
                tl_x = x - diff_w
                br_x = x + w
                tl_y = y
                br_y = y + h + diff_h
            elif x - diff_w >= 0:
                tl_x = x - diff_w
                br_x = x + w
                tl_y = y
                br_y = y + h
            elif y - diff_h >= 0:
                tl_x = x
                br_x = x + w
                tl_y = y - diff_h
                br_y = y + diff_h
            elif x + diff_w <= width_img:
                tl_x = x + diff_w
                br_x = x + w
                tl_y = y
                br_y = y + h
            elif y + diff_h <= height_img:
                tl_x = x
                br_x = x + w
                tl_y = y
                br_y = y + h + diff_h
        else:
            tl_x = x 
            br_x = x + w
            tl_y = y
            br_y = y + h
        #print(tl_x, tl_y, br_x, br_y)
        tmp_img = image[tl_y:br_y, tl_x:br_x]           #Crop image
        cv2.imwrite('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/tmp/tmp.png', tmp_img) #Create temporary image

        cv2.imwrite('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/cropped_tmp/' +str(counter)+'.png', tmp_img)
        analysis = reader.readtext('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/tmp/tmp.png')
        for i in analysis:
            if "cookie" in i[1].lower() or "cookies" in i[1].lower() or "küpsis" in i[1].lower() or "küpsised" in i[1].lower():
                patterns = analyse_pattern(analysis, tmp_img)                                     #Initiate function for pattern analysis
                os.remove('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/tmp/tmp.png')
                print('Cookie!')
                return True, patterns
        os.remove('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/tmp/tmp.png')
    print("No cookie...")
    return False, []

def analyse_pattern(list, image):
    patterns = []
    list = list
    image = image
    path = 'C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/tmp/tmp.png'
    accept = False
    reject = False
    settings = False
    accept_coord_tl = ()
    accept_coord_br = ()
    reject_coord_tl = ()
    reject_coord_br = ()
    settings_coord_tl = ()
    settings_coord_br = ()
    for i in list:
        if 'accept' in i[1].lower() or 'allow' in i[1].lower() or 'agree' in i[1].lower() or 'acknowledge' in i[1].lower() or 'consent' in i[1].lower() or 'nõustun' in i[1].lower() or 'luban' in i[1].lower():
            accept = True
            accept_coord_tl = tuple(i[0][0])
            accept_coord_br = tuple(i[0][2])
            accept_center = ((accept_coord_br[0]-accept_coord_tl[0])/2), ((accept_coord_br[1]-accept_coord_tl[0])/2)
        if 'reject' in i[1].lower() or 'decline' in i[1].lower() or 'keeldu' in i[1].lower() or 'disallow' or 'ei nõustu' in i[1].lower():
            reject = True
            reject_coord_tl = tuple(i[0][0])
            reject_coord_br = tuple(i[0][2])
        if 'settings' in i[1].lower() or 'more' in i[1].lower() or 'customize' in i[1].lower() or 'preferences'in i[1].lower() or 'manage' in i[1].lower() or 'sätted' in i[1].lower():
            settings = True
            settings_coord_tl = tuple(i[0][0])
            settings_coord_br = tuple(i[0][2])
            settings_center = ((settings_coord_br[0]-settings_coord_tl[0])/2), ((settings_coord_br[1]-settings_coord_tl[1])/2)
    if accept == True and reject == True:
        if accept_coord_tl[1] < accept_coord_br[1] and accept_coord_tl[0] < accept_coord_br[0] and reject_coord_br[1] > reject_coord_tl[1] and reject_coord_br[0] > reject_coord_tl[0] and reject_coord_tl[0] >= 0 and reject_coord_tl[1] >= 0:
            new_temp = cv2.imread(path)
            pos_temp = new_temp[int(accept_coord_tl[1]):int(accept_coord_tl[1]+2), int(accept_coord_tl[0]):int(accept_coord_br[0])]
            print(int(accept_coord_tl[1]), int(accept_coord_br[1]), int(accept_coord_tl[0]), int(accept_coord_br[0]))
            '''print(accept_coord_br[1], accept_coord_tl[1])
            print(accept_coord_br[0], accept_coord_tl[0])
            print(pos_temp)'''
            cv2.imwrite('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/tmp/pos_temp.png', pos_temp)
            new_temp = cv2.imread(path)
            neg_temp = new_temp[int(reject_coord_tl[1]):int(reject_coord_tl[1]+2), int(reject_coord_tl[0]):int(reject_coord_br[0])]
            print(int(reject_coord_tl[1]),int(reject_coord_br[1]), int(reject_coord_tl[0]),int(reject_coord_br[0]))
            '''print(reject_coord_tl[1], reject_coord_br[1])
            print(reject_coord_tl[0], reject_coord_br[0])
            print(neg_temp)'''
            cv2.imwrite('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/tmp/neg_temp.png', neg_temp)
            color_pos = ColorThief('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/tmp/pos_temp.png')
            color_neg = ColorThief('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/tmp/neg_temp.png')
            try:
                dominant_pos = color_pos.get_color(quality=1)
            except:
                dominant_pos = (255, 255, 255)
            print(dominant_pos)
            try:
                dominant_neg = color_neg.get_color(quality=1)
            except:
                dominant_neg = dominant_pos
            if dominant_pos != dominant_neg:
                patterns.append('Interference')
                print('Interference!')
            os.remove('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/tmp/pos_temp.png')
            os.remove('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/tmp/neg_temp.png')
            if settings == True:
                dist = sqrt((settings_center[0]-accept_center[0])**2+(settings_center[1]-accept_center[1])**2)
                if dist >= 200:
                    patterns.append('Sneaking')
        else:
            print('Image crop error')
            patterns.append('Image crop error')
            return patterns
    elif accept == True and reject == False:
        patterns.append('Obstruction')
        if settings == True:
            dist = sqrt((settings_center[0]-accept_center[0])**2+(settings_center[1]-accept_center[1])**2)
            if dist >= 200:
                patterns.append('Sneaking')
    elif accept == False:
        if settings == True:
            patterns.append('Obstruction')
        else:
            patterns.append('Unknown')
    return patterns

#Image_path -> filename.png
for image_path in os.listdir(image_folder):
    image = os.path.join(image_folder, image_path).replace("\\", "/") #Image -> file path
    name = image.split('\\')[-1].split('.')[0].capitalize()
    img = cv2.imread(image)                                           #Image file
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #Convert to gray
    detect_cookies = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(20,20)) #Detect cookies via Cascade
    detect_cookies = _group_rectangles(detect_cookies)  #Call custom function to group results

    cookie_results = find_cookies(detect_cookies, image, counter)

    if cookie_results[0]:
        counter += 1
        pattern_list = cookie_results[1]
        result = True
        save_to_file(name, image, result, pattern_list)
    else:
        counter += 1
        pattern_list = []
        result = False
        save_to_file(name, image, result, pattern_list)


    '''for (x, y, w, h) in detect_cookies:
        cv2.rectangle(img, (x, y),(x+w,y+h), (0, 255, 0), 2)

    
    cv2.imshow('Cookies', img)
    cv2.waitKey(0)
'''
