# we are using webcam .

import cv2
import numpy as np
cap = cv2.VideoCapture(0)  # we are accessing first webcam of the system
# cap = cv2.VideoCapture(1)     # to access for second webcam

while True:
    ret , frame = cap.read()
    
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)   # CHANGE the color into black&white
    cv2.imshow ('colored_WebCam',frame)
    cv2.imshow ('gray_WebCam',gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()   # this releases the 'capture' so that camera will be released
cv2.destroyAllWindows()   # to close all the window 

