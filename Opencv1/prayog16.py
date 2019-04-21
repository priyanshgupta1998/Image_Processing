# Image Aithmetics And Logics
#Ipose images on the another images.
#img1.shape = 320 x 400
# img2.shape = 493 x 500

import cv2
import numpy as np

img1 = cv2.imread( "C:\\Users\\PRIYANSH\\Desktop\\Images\\dog1.jpg" , cv2.IMREAD_COLOR)   # colored image
img2 = cv2.imread( "C:\\Users\\PRIYANSH\\Desktop\\Images\\py_logo0.jpg" , cv2.IMREAD_COLOR)   # colored image


rows , cols ,channels = img1.shape
reg_of_image = img2[0:rows , 0:cols]

img2gray = cv2.cvtColor(img2 , cv2.COLOR_BGR2GRAY)
ret , mask = cv2.threshold(img2gray , 220,255,cv2.THRESH_BINARY_INV)   # if color>220 then it will be considered as 'BLACK' or '0'
#ret , mask = cv2.threshold(img2gray , 220,255,cv2.THRESH_BINARY)   # if color>220 then it will be considered as '  WHITE' or '1'
# Here mask is altered  modified image of img2.



    



cv2.imshow('pYTHON_lOGO_Image', reg_of_image)     # Resolution will be same as pevious  #  opaqueness will also  be same 
cv2.waitKey(0)    # wait for the user (for infinite time) to press the EXIT /ESC key to close the window  
cv2.destroyAllWindows()   # close all the windows 


