import os
import easyocr

reader = easyocr.Reader(['en', 'et'], gpu=True)
directory = r"C:\Users\Thomas\Documents\Thesis\Image analysis\Analysed images"

datafile = open('C:/Users/Thomas/Documents/Thesis/Image analysis/worddata.txt', 'w')

dictionary = {} #Create empty dictionary

print("Starting to read data")
for file in os.listdir(directory):
    path = os.path.join(directory, file) #Create absolute path to image file
    result = reader.readtext(path)       #Analyse image
    for i in result:            
        if i[-1] >= 0.80:                #Check if word/phrase probability corresponds to threshold
            phrase = i[1]
            if ' ' in phrase:            #Check if it's a phrase by identifying spaces
                words = phrase.split(' ')   #If it's phrase cut it into words
                for word in words:
                    word = ''.join(letter for letter in word if letter.isalnum()) #Remove special characters, that may have passed
                    word = word.lower()         #Make all letters small
                    if word not in dictionary:  #Create and add to dictionary or increase given word count
                        dictionary[word] = 0
                    dictionary[word] += 1
            else:
                phrase = ''.join(letter for letter in word if letter.isalnum())
                phrase = phrase.lower()
                if phrase.lower() not in dictionary:
                    dictionary[phrase.lower()] = 0
                dictionary[phrase.lower()] += 1


dictionary = dict(sorted(dictionary.items(), key=lambda x:x[1], reverse=True)) #Sort dictionary by most common word
for a, b in dictionary.items():
    a.split()
    datafile.write('%s: %s\n' % (a, b)) #Write results to text file
