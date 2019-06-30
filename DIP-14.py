import cv2

img1=cv2.imread("n.jpg")
cv2.imshow('original image',img1)

"""
R=img1[:,:,0]
G=img1[:,:,1]
B=img1[:,:,2]
"""

R,G,B = cv2.split(img1)

oimg=img1

oimg[:,:,0]=B
oimg[:,:,2]=R

cv2.imshow("R and B Exchanged",oimg)
