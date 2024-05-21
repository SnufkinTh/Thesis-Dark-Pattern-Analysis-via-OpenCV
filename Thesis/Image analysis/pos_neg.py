import csv
import shutil

data = open('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/advanced_image_data_fortune_500_america.csv', 'r')
neg = open('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/negative.txt', 'w')
pos = open('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/positive.txt', 'w')

csvreader = csv.reader(data)
next(csvreader)

for i in csvreader:
    if i != []:
        if i[-1] == 'True':
            pos.write(i[1] + '\n')
            #shutil.copy(i[1], 'C:/Users/thoma/Documents/Thesis/Image analysis/positive') #Copy into folder with positive images
        else:
            neg.write(i[1]+ '\n')
            #shutil.copy(i[1], 'C:/Users/thoma/Documents/Thesis/Image analysis/negative') #Copy into folder with negative images