import cv2

cap = cv2.VideoCapture(0)

#There are different properties...
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,320) # associated No. , value of it...
cap.set(4,320) # camera will set its value acc. to it.

while(cap.isOpened()):
	ret, frame =cap.read()

	if ret ==True:
                
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('Gray Frame', gray)

                if cv2.waitKey(1) == ord('q'):
                        break
	else:
		break

cap.release()
cv2.destroyAllWindows()
