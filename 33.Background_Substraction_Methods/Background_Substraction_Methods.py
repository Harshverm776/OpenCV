# Background subtraction is a common and widely used technique for generating the foreground mask(which is also known as the binary image containing the pixels which belong to the moving object of a scene when the images are captured using a static camera).
# It perform the subtraction of the current frame and the background model of the scene.
# It can be used for - 1. Visitor counter 2. Traffic camera
# There are several algorithm for background subtraction-

# 1. cv2.bgsegm.createBackgroundSubtractorMOG() - very little noise

# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture('vtest.avi')
#
# fgbg = cv.bgsegm.createBackgroundSubtractorMOG() # Background Subtractor MOG method is a gaussian mixture based background and foreground segmentation algorithm.
# #Using this line we are creating background object of the function. It has some optional parameters.
#
# while True:
#     ret, frame = cap.read()
#     if frame is None:
#         break
#     fgmask = fgbg.apply(frame)
#
#     cv.imshow('Frame', frame)
#     cv.imshow('FG mask Frame', fgmask)
#     keyboard = cv.waitKey(30)
#     if keyboard == 'q'  or keyboard == 27 :
#         break
# cap.release()
# cv.destroyAllWindows()

# 2. cv2.createBackgroundSubtractorMOG2()

# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture('vtest.avi')
#
# fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=True) # It also detect shadow. There are certain parameters like detectShadows- by default it will be true
#
# while True:
#     ret, frame = cap.read()
#     if frame is None:
#         break
#     fgmask = fgbg.apply(frame)
#
#     cv.imshow('Frame', frame)
#     cv.imshow('FG mask Frame', fgmask)
#     keyboard = cv.waitKey(30)
#     if keyboard == 'q'  or keyboard == 27 :
#         break
# cap.release()
# cv.destroyAllWindows()

# 3. cv2.bgsegm.createBackgroundSubtractorGMG() -It is not good as 1st method.

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')

fgbg = cv.bgsegm.createBackgroundSubtractorGMG() # It combine statistical background image estimation and pre-pixel baissian segmentation.
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel) # For removing noise

    cv.imshow('Frame', frame)
    cv.imshow('FG mask Frame', fgmask)
    keyboard = cv.waitKey(30)
    if keyboard == 'q'  or keyboard == 27 :
        break
cap.release()
cv.destroyAllWindows()

# 4. cv2.createBackgroundSubtractorKNN()

# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture('vtest.avi')
#
# fgbg = cv.createBackgroundSubtractorKNN()  # It also detect shadow. There are certain parameters like detectShadows- by default it will be true
#
# while True:
#     ret, frame = cap.read()
#     if frame is None:
#         break
#     fgmask = fgbg.apply(frame)
#
#     cv.imshow('Frame', frame)
#     cv.imshow('FG mask Frame', fgmask)
#     keyboard = cv.waitKey(30)
#     if keyboard == 'q'  or keyboard == 27 :
#         break
# cap.release()
# cv.destroyAllWindows()