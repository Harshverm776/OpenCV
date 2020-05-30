import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg',-1)
cv2.imshow('image',img)
c_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#plt.imshow(img) # Output : The matplot image will be of different color since the opencv uses BGR format and matplot uses RGB format.
plt.xticks([]), plt.yticks([]) # Hiding the ticks , passing empty array...

plt.imshow(c_img)
plt.show()
 
cv2.waitKey(0)
cv2.destroyAllWindows()
