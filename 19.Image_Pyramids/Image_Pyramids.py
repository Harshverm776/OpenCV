# It can be use for finding faces/ objects of different resolution.
# Types-
# 1.) Gaussian , 2.) Laplacian
import cv2
import numpy as np

img = cv2.imread('lena.jpg')
layer = img.copy()
gp = [layer]

# pyrDown() and pyrUp() can be use for Gaussian
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow("upper level Gaussain Pyramid", layer)
lp = [layer]

# Laplacian is formed by difference between that level in gaussain pyramid and expanded version of its upper level in gaussain pyramid.
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

# Laplacian & Gaussain Pyramid are used for Blend and Reconstruction of images.

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()