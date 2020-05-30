# Canny Edge Detection is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges.
# It contain five different steps.
import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

cv2.namedWindow('Image')
cv2.createTrackbar('Thresold1', 'Image', 0, 255, nothing)
cv2.createTrackbar('Thresold2', 'Image', 0, 255, nothing)

# This image will be more better.

while (1):
    img = cv2.imread('messi5.jpg', 0)
    th1 = cv2.getTrackbarPos('Thresold1', 'Image')
    th2 = cv2.getTrackbarPos('Thresold2', 'Image')

    if cv2.waitKey(1) == 27:
        break

    canny = cv2.Canny(img, th1, th2)  # image,thresold-1, thresold-2
    cv2.imshow('Image', canny)

cv2.destroyAllWindows()
