import cv2
import os

image_folder = r'C:\Users\/thoma\Documents\Thesis_new\Thesis\Image analysis\positive'
cascade = cv2.CascadeClassifier('C:/Users//thoma/Documents/Thesis_new/Thesis/Image analysis/training_result/cascade.xml')

for image_path in os.listdir(image_folder):
    image = os.path.join(image_folder, image_path).replace("\\", "/")
    print(image)
    img = cv2.imread(image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #konverteerime must-valgeks
    cookies = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(20,20))
    result = cv2.groupRectangles(cookies, 0, 0.75)
    print(result)

    for(x, y, w, h) in result[0]: #result tagastab suure array milles on leitud objekti x, y - algpunkti koordinaadid; w,h - pikkus ja kõrgus
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Cookies', img)
    cv2.waitKey(0)


#cd 'image analysis'
#C:/Users/Thomas/Documents/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data training_result/ -vec pos.vec -bg neg.txt -w 48 -h 48 -numPos 170 -numNeg 350 -numStages 9 -maxFalseAlarmRate 0.25 -precalcValBufSize 5000  -precalcIdxBufSize 5000 -minHitRate 0.985

#C:/Users/Thomas/Documents/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=positive/ -m=1

#C:/Users/Thomas/Documents/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -number 1000 -vec pos.vec

#Good results with 12 stages 24x24 0.99 max and 0.175 lower