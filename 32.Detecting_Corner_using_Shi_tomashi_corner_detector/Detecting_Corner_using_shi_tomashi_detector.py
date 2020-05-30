# Shi tomashi is a small modification to Harris corner detector.
# It give better result in comparison to Harris corner detector.
# We can provide number of corner we want.
import numpy as np
import cv2 as cv

img = cv.imread('pic1.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 25, .01, 10) # Image, Maximum no of corners(strongest corner will be returned), Quality level, minDistance
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x,y), 3, 255, -1)

cv.imshow('dst', img)

if cv.waitKey(0) & 0xff == 27 :
    cv.destroyAllWindows()