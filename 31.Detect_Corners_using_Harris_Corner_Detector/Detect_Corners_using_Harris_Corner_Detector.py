# Harris Corner Detector
# Corners are regions with large variation in the intensity in all the directions.
# It contains three main steps :
# 1. Determine which windows produce very large variations in intensity when moved in both X and Y directions.
# 2. With each such window found a score R is computed.
# 3. After applying a threshold to this score, important corners are selected & marked.
# There are different conditions of R which determine - Flat region, Edge, and Corner.
import numpy as np
import cv2 as cv

img = cv.imread('chessboard.png')

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray) # CornerHarris method read image in float format therefore convertion is taken place.
dst = cv.cornerHarris(gray, 2, 3, 0.04) # image, blockSize - It is the size of neighbourhood considered for corner detection, ksize - Aperture parameter of sobel derivative, k - harris detector free parameter.

dst = cv.dilate(dst, None) # for better result

img[dst > 0.01 * dst.max()] = [0, 0, 255] # threshold and coloration

cv.imshow('dst', img)

if cv.waitKey(0) & 0xff == 27 :
    cv.destroyAllWindows()
