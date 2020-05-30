import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)  # You can use LinuxLogo.jpg for more clarification
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((3, 3), np.uint8)  # white square

dilation = cv2.dilate(mask, kernal,
                      iterations=2)  # Source, kernel- some shape, iteration- no. of iterations its default value is one
erosion = cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)  # erosion then dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)  # dilation then erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)  # difference between dilation and erosion
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)  # difference between image and opening

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
