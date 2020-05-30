# There are two types of Hough Lines Transforms:-
# 1. Standard Hough Transform
# 2. Probabilistic Hough Line Transform
import cv2
import numpy as np

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
cv2.imshow('Canny', edges)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200) # Image, rho- distance resolution of the accumulator in pixels, theta- Angle resolution of the accumulator in radians, thresold
# These lines will be of infinite length
# These problem can be solved using HoughLinesP method
# conversion of polar coordinates to cartesian coordinates
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho 
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1,y1), (x2,y2), (0, 0, 255), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()