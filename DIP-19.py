import cv2
import numpy as np


from matplotlib import pyplot as plt

def rgb2gray(rgb):
    r,g,b=rgb[:,:,0],rgb[:,:,1],rgb[:,:,2]
    gray=0.2989 * r +0.5870*b
    gimg=np.uint8(np.round(gray))
    return gimg

#original image

img=cv2.imread("n.jpg")
cv2.imshow('original image',img)


#writen function to convert from rgb to gray
gimg=rgb2gray(img)
cv2.imshow('gray image',gimg)

h=np.zeros(256)
[m,n]=np.shape(gimg)

for i in range(m):
    for j in range(n):
        h[gimg[i][j]]=h[gimg[i][j]]+1
   
#plt.plot(h)
#plt.show()



#hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
#plt.hist(h.ravel(),256,[0,256])
print(h)
print(sum(h))
print(m*n)
plt.hist(h)
plt.title('Histogram for gray scale picture')
plt.show()

pdf=h/(m*n)
print(pdf)

#plt.hist(pdf.ravel(),256,[0,256])
plt.plot(pdf)
#ax2.plot(pdf)
plt.title('pdf for gray scale picture')
plt.show()

cdf=pdf



for i in range(1,256):
    cdf[i]=cdf[i]+cdf[i-1]
print(cdf)
plt.plot(cdf)
#ax3.title('cdf for gray scale picture')
plt.show()

en2img=gimg
for i in range(m):
    for j in range(n):
        en2img[i][j]=np.uint8(255.0*cdf[gimg[i][j]])

cv2.imshow('2_Enhanced image',en2img)



#def hisequ(gimg):
# return (eqimg)



cv2.waitkey(0)
cv2.destroyAllWindows()
