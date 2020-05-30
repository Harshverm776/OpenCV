# change colors using trackbar using switch.
import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

img = np.zeros((300,512,3),np.uint8)
cv.namedWindow('image') # Create a window with name 'image'

cv.createTrackbar('B', 'image', 0, 255, nothing) # Trackbar_Name, Window_Name, initial_value, Final_value, call_back_function
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON' # Name of switch as a trackbar
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image',img)
    if cv.waitKey(1) == 27:
        break

    b = cv.getTrackbarPos('B','image') # trackbar, window
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')
    s = cv.getTrackbarPos(switch,'image')

    if s ==0:
        img[:] = 0
    else:
        img[:] = [b, g, r] # set this color to img
        
cv.destroyAllWindows()
