from colorthief import ColorThief

def poop():
    list = []
    list.append('a')
    list.append('b')
    list.append('c')
    return list

color = ColorThief('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/pos36.png')
color1 = ColorThief('C:/Users/thoma/Documents/Thesis_new/Thesis/Image analysis/neg36.png')
dominant = color.get_color(quality=10)
dominante = color1.get_color(quality=10)

print(dominant)
print(dominante)


cat = poop()
print(cat)