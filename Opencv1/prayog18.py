# Image Aithmetics And Logics
#Ipose images on the another images.
# Now i'll use the concept of THRESHOLD to define  the range of the color


import cv2
import numpy as np

img = cv2.imread( "C:\\Users\\PRIYANSH\\Desktop\\Images\\bookpage.jpg" )   # colored image

#convert into gray image
gray = cv2.cvtColor(img ,  cv2.COLOR_BGR2GRAY)

#Simple Threshold
retval , simp_threshold = cv2.threshold(gray , 12 , 255 , cv2.THRESH_BINARY)

#Sue threshold    # worst method 
retval , otsu = cv2.threshold(gray , 125 , 255 , cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#gaussion adaptive threshold      :  # Best method
gaus = cv2.adaptiveThreshold(gray , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY,115,1)


cv2.imshow('ambiguous_image_simp', simp_threshold)
cv2.imshow('ambiguous_image_OTSU', otsu)   
cv2.imshow('ambiguous_image_gaus', gaus)   # can read the content which is written on the page 
cv2.waitKey(0)    # wait for the user (for infinite time) to press the EXIT /ESC key to close the window  
cv2.destroyAllWindows()   # close all the windows 













































