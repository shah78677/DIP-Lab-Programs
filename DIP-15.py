import cv2

img1=cv2.imread("11.jpg")
img2=cv2.imread("22.jpg")

gimg1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) 
gimg2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

cv2.imshow('1original image',img1)
cv2.imshow('2original image',img2)

cv2.imshow('1grey image',gimg1)
cv2.imshow('2grey image',gimg2)

cc=img1 & img2
cv2.imshow('combined color image',cc)

aa=gimg1 & gimg2
cv2.imshow('combined image',aa)

occ=img1 | img2
cv2.imshow('OR combined color image',occ)

oaa=gimg1 | gimg2
cv2.imshow('OR combined image',oaa)


xocc=img1 ^ img2
cv2.imshow('XOR combined color image',xocc)

xoaa=gimg1 ^ gimg2
cv2.imshow('XOR combined image',xoaa)

ncc=~img1 
cv2.imshow('NOT combined color image',ncc)

naa=~gimg1 
cv2.imshow('NOT combined image',naa)

cv2.waitkey(0)
cv2.destroyAllWindows()
