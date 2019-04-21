#Corner Detection
#it can be used for motion tracking

import numpy as np
import cv2

img = cv2.imread('C:\\Users\\PRIYANSH\\Desktop\\Images\\opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)    # 100 cordinates which are  the corners

corners = np.int0(corners)   # convert into integer 


for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3, 255, -1)
    
cv2.imshow('Corners',img)


