import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# for Homogeneous filter
kernal = np.ones((5, 5), np.float32) / 25 # is a shape which can apply on an image
# Homogeneous filter- Simplest- each output pixel is the mean of its kernal neighbors
dst = cv2.filter2D(img, -1, kernal) # image, desired_depth, kernel

# Blur method - also called averaging
blur = cv2.blur(img, (5, 5)) # image, kernel

# Gaussian Filter using different weight kernel in x,y direction
gblur = cv2.GaussianBlur(img, (5, 5), 0) # image, kernel, sigma-x Value
# It is design for removing high frequency noise

# Median filter - replace each pixels value with the median of its neighbouring pixels.
# great for 'salt and pepper noise'
median = cv2.medianBlur(img, 5) # image, kernel size -must be odd except one.

# Bilateral Filter- used for preserved edges while bluring.
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75) # image, diameter of neighouring pixels, sigma color, sigma space
titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
