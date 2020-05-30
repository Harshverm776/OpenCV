import cv2
import numpy as np
img = cv2.imread("messi5.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("messi_face.jpg", 0)
w, h = template.shape[::-1] # column and row values in reverse order

res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED) # image, template, method
print(res) # matrix - there will be a brightest point in  this matrix - from this matrix we will get the top left most point
threshold = 0.91
loc = np.where(res >= threshold)
print(loc) # point/ points
for pt in zip(*loc[::-1]): # multiple matched templates / zip- reversing the x-y axis
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()