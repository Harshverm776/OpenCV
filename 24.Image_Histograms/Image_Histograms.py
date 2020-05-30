# Histograms are graph which give the overall intensity distribution of an image.
# There are several ways of finding histogram.

# 1. matplotlib :
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
#
# img = np.zeros((200, 200), np.uint8) # black image
# cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv.rectangle(img, (0, 50), (100, 100), (127), -1)
#
# plt.hist(img.ravel(), 256, [0, 256]) # image, max no of pixel values, range
# plt.show()
#
# cv.waitKey(0)
# cv.destroyAllWindows()

# 2 For intensity distribution for different colors :
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
#
# img = cv.imread("lena.jpg")
#
# b, g, r = cv.split(img)
#
# cv.imshow("img", img)
# cv.imshow("b", b)
# cv.imshow("g", g)
# cv.imshow("r", r)
#
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
#
# plt.show()
#
# cv.waitKey(0)
# cv.destroyAllWindows()

# 3. calchist in cv2
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("lena.jpg",0)
hist = cv.calcHist([img], [0], None, [256], [0, 256]) # image in sq brackets, index of channel, mask - none for full image, hist size, range
plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
# Uses of histograms:
# 1. It can tell us whether the image is properly exposed like in digital image
# 2. Whether the lighting conditions was harsh or flat.
# 3. We can make adjustment in image