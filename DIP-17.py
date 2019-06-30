import cv2
import numpy as np


img=cv2.imread("lena-binary.jpg",0)
cv2.imshow('original image',img)

print(np.shape(img))
[m,n]=np.shape(img)
edimage=img.copy()
ed2image=img.copy()

#-1-2-1
#000
#121
for x in range(1,m-1):
    for y in range(1,n-1):
        edimage[x][y]=((img[x-1][y+1]+(2*img[x][y+1])+img[x+1][y+1]) - (img[x-1][y-1]+(2*img[x][y-1])+img[x+1][y-1]))

#-1 0 1
#-2 0 2
#-1 0 1

for x in range(1,m-1):
    for y in range(1,n-1):
        ed2image[x][y]=(((-1*img[x-1][y+1])+img[x+1][y+1] + (-2*img[x-1][y])+(2*img[x+1][y])  + (-1*img[x-1][y-1])+img[x+1][y-1]))
    
canny_img = edimage & ed2image
cv2.imshow('Canny filter horizontal image',edimage)
cv2.imshow('Canny filter  vertical image',ed2image)
cv2.imshow('Canny filter image',canny_img)
