import cv2
import numpy as np

#img = cv2.imread('lena.jpg',1)

#creat img using numpy zeros method
img = np.zeros([512,512,3],np.uint8) # [H,W,3], Data Type

# color (B,G,R)
img = cv2.line(img,(0,0),(255,255),(255,0,0),3) # 1,2,3.... Thickness

img = cv2.arrowedLine(img,(0,255),(255,300),(255,0,0),5)

img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),4) # -1 for filling it

img =cv2.circle(img,(447,63),63,(0,255,0),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCv',(10,500),font,4,(255,255,255),10,cv2.LINE_AA)

cv2.imshow('Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
