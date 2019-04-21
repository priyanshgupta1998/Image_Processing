# Color Filtering
# using HSV (hue satutaiton value )

import cv2
import numpy as np

cap = cv2.VideoCapture(0)   # select the first camera in the system

while True:
    _ , frame = cap.read()
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    # Now filter the video ( remove Noise , and )
    # The idea is  detect the unique color in the video streaming

    lower_red = np.array([0,153,0])    
    upper_red = np.array([153,200,255])

    mask = cv2.inRange(hsv , lower_red , upper_red)  # select a unique color

    result = cv2.bitwise_and(frame , frame  , mask =mask )


    cv2.imshow ( 'frame ' , frame )
    cv2.imshow('mask', mask)
    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
    
    



































