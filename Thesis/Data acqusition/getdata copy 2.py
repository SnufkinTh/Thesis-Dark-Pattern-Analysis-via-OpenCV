


#File to write links into
'''file = open("Data acqusition/Data/global_links.txt", 'r')

lines = file.readlines()
for line in lines:
    print(line)'''

file = open("Data acqusition/Data/global_links.txt", 'r', encoding='UTF-8')
filew = open("Data acqusition/Data/new_links.txt", 'w', encoding='UTF-8')

lines = file.readlines()

list = []

for line in lines:
    a = line.split(' ')
    for i in a:
        i = line.split('\t')
        for j in i:
            if j.startswith('www') and j not in list:
                list.append(j)

for link in list:
    filew.write('https://'+link + '\n')

file.close()
filew.close()