# Mean Shift -
# 1. Pass initial location of target object and the histogram back projection image to mean shift function.
# 2. As the object move the histogram projected image also changes.
# 3. The mean shift function move the window to the new location with the maximum probability dentsity.

# Tracking the window of a white car.
import numpy as np
import cv2 as cv
cap = cv.VideoCapture('slow_traffic_small.mp4')

# Take first frame of the video
ret, frame = cap.read()

# Setup initial location of window
x, y, width, height = 300, 200, 100, 50
track_window = (x, y, width, height)

# Setup the ROI for tracking
roi = frame[y: y+height, x:x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255))) # It is also for removing low light values.
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX) # source, destination, alpha, beta, norm_type

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt.
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1) # termination criteria, term criteria till 10 points, atleast 1 point
cv.imshow('roi',roi)
while(1):
    ret, frame = cap.read()
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1) # No of images, channels, hist_value, ranges, scale

        # Apply meanshift to get the new location
        ret, track_window = cv.meanShift(dst, track_window, term_crit) # image, track image, termination criteria

        # Draw it on image
        x, y, w, h = track_window
        final_image = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 3)

        cv.imshow('dst', dst)
        cv.imshow('final_image', final_image)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

# Disadvantage -
# 1. We have to pass the initial position of the traget window.
# 2. The size of the target window doesn't change.
