# Image Aithmetics And Logics
import cv2
import numpy as np

img1 = cv2.imread( "C:\\Users\\PRIYANSH\\Desktop\\Images\\dog1.jpg" , cv2.IMREAD_COLOR)   # colored image
img2 = cv2.imread( "C:\\Users\\PRIYANSH\\Desktop\\Images\\rabbit.jpg" , cv2.IMREAD_COLOR)   # colored image

add = img1 +img2

# Add two images by using opencv 
add = cv2.add(img1,img2)   # BGR order ofcolors

cv2.imshow('Cat_dog_image',add)   # Resolution will be same as pevious #  opaqueness will also  be same 
cv2.waitKey(0)    # wait for the user (for infinite time) to press the EXIT /ESC key to close the window  
cv2.destroyAllWindows()   # close all the windows 


