import os
from math import ceil, floor
from PIL import Image, ImageDraw, ImageColor, ImageFile

im = Image.open(os.path.join('../asciiProj/0.jpg')) 
charASCII = "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1}{[]?-_+~<>i!lI;:,\"^`'. "  # Darkest char to brightest char
File_object = open(os.path.join("../asciiProj/text.txt"), "w") # Text file
pixels = list(im.getdata())
width, height = im.size
ratio = 255/(len(charASCII)-1)
matrix = []
i = 0

for y in range(height):
    sOne = ''.join(matrix)
    sTwo = '\n'
    L = [sOne, sTwo]
    File_object.writelines(L)
    #print(sOne)
    matrix = []
    for x in range(width):
        brightness = ceil((pixels[i][0]+pixels[i][1]+pixels[i][2])/3)
        for j in range(2):
            matrix.append(charASCII[floor(brightness/ratio)])
        i += 1

File_object.close()
print('Done!')