import cv2

cap = cv2.VideoCapture(0) # File Name or Device index from which me want to read like 0(Default),-1,1...
fourcc = cv2.VideoWriter_fourcc(*'XVID') # or like ('X','V','I','D')
# http://fourcc.org/codecs.php
out = cv2.VideoWriter('output.avi',fourcc,20.0, (640,480)) # (output,fourcc code, no. of frame per sec,size)

print( cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Properties....
print( cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


while(True): # while(cap.isOpened()) return False is index or address is not correct. Also we can use cap.Open()
	ret, frame =cap.read()

	if ret ==True:	
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		out.write(frame) # Writing New Video (Making)
		cv2.imshow('Colored Frame', frame) # Colored
		cv2.imshow('Gray Frame', gray) # Gray

		if cv2.waitKey(1) == ord('q'): # if q is pressed then come out from the loop. 
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()

