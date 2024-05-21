import csv
import re

pos = []
neg = []
pat = []
#data = open('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/solution_data_new.csv', 'r')
data = open('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/solution_data_new_fortune_global.csv', 'r')
csvreader = csv.reader(data)
next(csvreader)

for i in csvreader:
    if i != []:
        if i[-2] == 'True':
            pos.append(i[0])
            pat.append(i[-1])
        else:
            neg.append(i[0])

mat = []
for i in pat:
    mat.append(re.findall(r"'(.*?)'", i, re.DOTALL))

hat = []

for i in mat:
    for j in i:
        hat.append(j)


print(hat)
print('Positive files: ', len(pos))
print('Negative files: ', len(neg))
print('Empty: ', mat.count([]))
print('Interference: ', hat.count('Interference'))
print('Sneaking: ', hat.count('Sneaking'))
print('Obstruction: ', hat.count('Obstruction'))
print('Unknown', hat.count('Unknown'))
