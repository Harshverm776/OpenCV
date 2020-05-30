# Coutours are the curve joining all the continues points along the boundaries which are having the same colors or intensity.
# They are useful tools for shape analysis or object detection or object recognition.
# For better result we generally use binary image for finding the contours.
import numpy as np
import cv2

img = cv2.imread("opencv-logo.png")
img = cv2.resize(img, (600,600))
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # (thresh, contour retrieval mode, method)
# Contours is a Python list of all the contours in the image. Each individual contour is a Numpy array of (x, y) coordinates of boundary points of the objects.
# Output vector which contain info about image topology.

print("Number of contours = " + str(len(contours)))
print(contours[0])
n = 0
while(True):
    cv2.drawContours(img, contours, n, (0, 200, 100), 2) # image, contours, contours indexes = -1 will draw all the contours, color,  thickness
    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('n'):
        n +=1
cv2.destroyAllWindows()