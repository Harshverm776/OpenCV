# Object detection using feature based Haar cascade classifier is a effective object detection method.
# It is ML based approach where a cascade function is trained for lot of positive and negative images.
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # from opencv github repository
#img = cv2.imread('sample1.jpg')
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)# image, scale factor - specify how much the image size is reduced at each image scale, minNeighbors - specify how many neighbours each candidate rectangle have to retain it.

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
