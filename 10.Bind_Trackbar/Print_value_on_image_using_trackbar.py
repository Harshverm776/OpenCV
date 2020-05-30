# Print value on image using trackbar and use switch to change the color of image to gray and vice-versa.

import numpy as np
import cv2 as cv

def nothing(x):
    pass

cv.namedWindow('image')
cv.createTrackbar('Value', 'image', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv.imread('lena.jpg')
    pos = cv.getTrackbarPos('Value','image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50,150), font, 6, (0, 0, 255), 10)
    
    if cv.waitKey(1) == 27:
        break

    s = cv.getTrackbarPos(switch,'image')

    if s == 0:
        pass # do nothing
    else:
        img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img = cv.imshow('image',img)
        
cv.destroyAllWindows()
