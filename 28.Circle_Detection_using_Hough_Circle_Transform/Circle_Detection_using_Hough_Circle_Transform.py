import numpy as np
import cv2 as cv
img = cv.imread('smarties.png')
output = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 11)
cv.imshow('gray', gray)

circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0) # return circle vector
# image, method - only one implemented i.e., Hough_Gradient,
# dp - Inverse ratio of the accumulator resolution to the image resolution - 1 means same resolution  - 2 means half width and hieght ,
# minDist - minimum distance between the centers of the detected circles,
# param1 -  is the higher threshold of the two passed to the canny edge detector,
# param2 - is the accumulator threshold for the circle centers at the detection stage,
# minRadius - minimum circle radius,
# maxRadius - maximum circle radius. If <= 0 uses the maximum image dimension. If < 0 returns centers without finding the radius.

detected_circles = np.uint16(np.around(circles)) # converting vector into integers
for (x, y, r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (0, 255, 0), 3) # for circle
    cv.circle(output, (x, y), 2, (0, 255, 255), 3) # for center

cv.imshow('output', output)
cv.waitKey(0)
cv.destroyAllWindows()