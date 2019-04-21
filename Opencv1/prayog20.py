# Color Filtering
# using HSV (hue satutaiton value )
# create Blurring image 

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

    kernel = np.ones((15,15) , np.float32 )/255  # getting numpy array of 15 x15
    smoothed = cv2.filter2D(result , -1 , kernel)

    # median Blur  # Best among of these  # less noisy 
    median = cv2.medianBlur(result , 15)

    # bilateral Blur
    bilateral = cv2.bilateralFilter(result , 15,75,75)   # less useful #too much noisy 

    # Gaussian Blur   # Best among of these 
    blur = cv2.GaussianBlur(result , (15,15),0)

    

    cv2.imshow ( 'frame ' , frame )
    cv2.imshow('mask', mask)
    cv2.imshow('result',result)
    cv2.imshow('Blury',smoothed)
    cv2.imshow('median',median)
    cv2.imshow('bilateral',bilateral)
    cv2.imshow('Gauss',gauss)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
    




    



































