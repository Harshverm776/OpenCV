import cv2
img = cv2.imread('lena.jpg',1)
print(img) 

cv2.imshow('image',img)
# Use cv2.waitKey(0) & 0xFF for 64 bit if you are not able to run it.
k = cv2.waitKey(0) # waitKey(5000) - wait for 5000 milli sec or 0 == wait till not closed

if k == 27:
	cv2.destroyAllWindows() # or destroyWindow() For particular window ...
elif k == ord('s'):
	cv2.imwrite('lena_copy.png',img)
	cv2.destroyAllWindows()
	