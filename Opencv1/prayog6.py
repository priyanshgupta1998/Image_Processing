import cv2
import numpy as np
import matplotlib.pyplot as plt

# In opencv we have one parameter 'alpha'  . alpha is used to control the opacity of the image # it is just opposite of transparency


img = cv2.imread( "C:\\Users\\PRIYANSH\\Desktop\\Images\\cat.jpg" , cv2.IMREAD_GRAYSCALE)  # 2nd parameter is used to remove the 'alpha'    # and we will get non colored image.

# value for colored image IMREAD_COLOR = 1
#  IMREAD_UNCHANGED = -1

cv2.imshow('Cat',img)
cv2.waitKey(0)    # wait for the user (for infinite time) to press the EXIT /ESC key to close the window  
cv2.destroyAllWindows()   # close all the windows 
cv2. imwrite("C:\\Users\\PRIYANSH\\Desktop\\datascience\\Opencv\\Output\Cat.jpg",img)   # save the image 
