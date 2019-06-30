import cv2
import numpy as np

def rgb2gray(rgb):
    r,g,b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * b
    gimg = np.uint8(np.round(gray))
    return gimg

def addnoise(img, per):
    [m,n] = np.shape(img)
    nv = np.uint16((m*n) * (per/100))

    for i in range(nv):
        x = np.random.randint(m)
        y = np.random.randint(n)

        if(i%2==0):
            img[x][y] = 0
        else:
            img[x][y] = 255

    return img

img = cv2.imread('n.jpg')
cv2.imshow('Original Image', img)

gimg = rgb2gray(img)
cv2.imshow('Gray Image', gimg)

nimage = addnoise(gimg, 10)
cv2.imshow('Noisy Image', nimage)

[m,n] = np.shape(nimage)

for i in range(1, m-1):
    for j in range(1, n-1):
        blk = nimage[i-1 : i+2, j-1 : j+2]
        nimage[i,j] = np.median(blk)

cv2.imshow('Median Filter', nimage)

for i in range(1, m-1):
    for j in range(1, n-1):
        blk = nimage[i-1 : i+2, j-1 : j+2]
        nimage[i,j] = np.mean(blk)

cv2.imshow('Mean Filter', nimage)

gaussian_image = cv2.GaussianBlur(nimage,(5,5),0)
cv2.imshow('Gaussian Filter', gaussian_image)
