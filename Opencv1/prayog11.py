# we will work on Region of image
# we willl take some part of the image and paste it somewhere elsse in the image.
# Save the output caputure vedio in the system.
import cv2
import numpy as np

img = cv2.imread( "C:\\Users\\PRIYANSH\\Desktop\\Images\\cat.jpg" , cv2.IMREAD_COLOR)   # colored image

# Draw a circle
cv2.circle(img , (620,250) , 140 , (0,214,98),1)   # grren circle  # (x,y)



# create the region
watch_face = img[50:370 ,450:780]    # img[vertical_cordinate_ranges , horizontal_cordinate_ranges]
img[0:320 , 0:330] = watch_face




cv2.imshow('Cat_image',img )
cv2.waitKey(0)    # wait for the user (for infinite time) to press the EXIT /ESC key to close the window  
cv2.destroyAllWindows()   # close all the windows 
