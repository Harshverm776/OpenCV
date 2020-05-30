# An image gradient is a directional change in the intensity or color in an image.
# It is use to find edge detection and there are several methods.
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png', cv2.IMREAD_GRAYSCALE)

# laplacian gradient
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3) # image, data_type, kernal_size
lap = np.uint8(np.absolute(lap)) # conversion

# SobelX Gradient
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) # image, data_type, dx-x direction - order of derivative, dy- y direction

# SobelY Gradient
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# Sobel Combine
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()