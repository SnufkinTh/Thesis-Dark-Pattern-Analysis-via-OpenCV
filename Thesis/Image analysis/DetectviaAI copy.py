import cv2
import os

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



image_folder = r'C:\Users\Thomas\Documents\Thesis\Image analysis\positive'
cascade = cv2.CascadeClassifier('C:/Users/Thomas/Documents/Thesis/Image analysis/training_result/cascade.xml')

for image_path in os.listdir(image_folder):
    image = os.path.join(image_folder, image_path).replace("\\", "/")
    img = cv2.imread(image)
    print(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #konverteerime must-valgeks
    cookies = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(20,20))
    cookies = list(cookies)
    cookies = _group_rectangles(cookies)
    
    print(cookies)

    '''for (x, y, w, h) in cookies:
        cv2.rectangle(img, (x, y),(x+w,y+h), (0, 255, 0), 2)
    
        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Cookies', img)
    cv2.waitKey(0)'''


#cd 'image analysis'
#C:/Users/Thomas/Documents/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data training_result/ -vec pos.vec -bg neg.txt -w 48 -h 48 -numPos 170 -numNeg 350 -numStages 9 -maxFalseAlarmRate 0.25 -precalcValBufSize 5000  -precalcIdxBufSize 5000 -minHitRate 0.985

#C:/Users/Thomas/Documents/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=positive/ -m=1

#C:/Users/Thomas/Documents/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -number 1000 -vec pos.vec

#Good results with 12 stages 24x24 0.99 max and 0.175 lower

#Works:
# C:/Users/Thomas/Documents/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data training_result/ -vec pos.vec -bg neg.txt -w 32 -h 32 -numPos 250 -numNeg 350 -numStages 10 -maxFalseAlarmRate 0.18 -precalcValBufSize 5000  -precalcIdxBufSize 5000 -minHitRate 0.985