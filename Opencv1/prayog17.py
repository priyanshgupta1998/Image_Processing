# Image Aithmetics And Logics
#Ipose images on the another images.
# Now i'll use the concept of THRESHOLD to define  the range of the color
#we can use threshold in opencv to split the image into two part (on the basis of color)

import cv2
import numpy as np

img1 = cv2.imread( "C:\\Users\\PRIYANSH\\Desktop\\Images\\dog1.jpg" , cv2.IMREAD_COLOR)   # colored image
img2 = cv2.imread( "C:\\Users\\PRIYANSH\\Desktop\\Images\\py_logo1.jpg" , cv2.IMREAD_COLOR)   # colored image


rows , cols ,channels = img2.shape   #python logo 
roi = img1[0:rows , 0:cols]   # image of dog 

img2gray = cv2.cvtColor(img2 , cv2.COLOR_BGR2GRAY)
ret , mask = cv2.threshold(img2gray , 220,255,cv2.THRESH_BINARY_INV)   # if color>220 then it will be considered as 'BLACK' or '0'
#ret , mask = cv2.threshold(img2gray , 220,255,cv2.THRESH_BINARY)   # if color>220 then it will be considered as '  WHITE' or '1'
# Here mask is altered  modified image of img2.

mask_inv = cv2.bitwise_not(mask)   # just opposite of mask

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)    #in the white region we will put img1 part (roi)and leave black as it 

img2_fg = cv2.bitwise_and(img2 , img2 , mask =mask)

dst = cv2.add(img1_bg , img2_fg)
img1[0:rows,0:cols] =dst




cv2.imshow('pYTHON_lOGO_Image0', mask)     # Resolution will be same as pevious  #  opaqueness will also  be same 
cv2.imshow('pYTHON_lOGO_Image1', mask_inv )
cv2.imshow('pYTHON_lOGO_Image3', img1_bg )
cv2.imshow('pYTHON_lOGO_Image_4', img2_fg  )
cv2.imshow('pYTHON_lOGO_Image_5', dst )
cv2.imshow('pYTHON_lOGO_Image_6', img1)
cv2.waitKey(0)    # wait for the user (for infinite time) to press the EXIT /ESC key to close the window  
cv2.destroyAllWindows()   # close all the windows 


