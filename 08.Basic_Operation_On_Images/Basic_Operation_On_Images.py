import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) # returns a tuple of number of rows,columns and channels
print(img.size) # returns Total number of pixels
print(img.dtype) # returns image datatype
b , g, r = cv2.split(img)

img = cv2.merge((b,g,r))

ball = img[280:340, 330:390] # copy ball
img[273:333, 100:160] = ball # paste ball

img = cv2.resize(img, (500, 500))
img2 = cv2.resize(img2, (500,500))

#dst = cv2.add(img, img2) # images should be of same size
dst = cv2.addWeighted(img, .8 ,img2, .2 , 0) # img1, weight, img2, weight, gamma value

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
