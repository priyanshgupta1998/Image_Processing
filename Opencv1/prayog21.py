# Morphological Transforamtions
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
  # create many blurs based on Noisy
    mask = cv2.inRange(hsv , lower_red , upper_red)  # select a unique color   # noisy 

    result = cv2.bitwise_and(frame , frame  , mask =mask )

    kernel = np.ones((5,5) , np.int8 )/255  # getting numpy array of 15 x15
    erosion = cv2.erode(mask , kernel,iterations =1)
    dilation = cv2.dilate(mask , kernel , iterations = 1)

    opening   = cv2.morphologyEx(mask , cv2.MORPH_OPEN ,kernel)
    closing  = cv2.morphologyEx(mask , cv2.MORPH_CLOSE ,kernel)


    cv2.imshow ( 'frame ' , frame )
    cv2.imshow('mask', mask)
    cv2.imshow('result',result)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
    




    




