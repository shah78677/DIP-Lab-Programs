import cv2
import numpy as np

img = cv2.imread('degrade_image.bmp',0)


kernel = np.array([[0,1,0],[1,1,1],[0,1,0]], np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)
#closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Original Image', img)
cv2.imshow('Morphological closing', dilation)
