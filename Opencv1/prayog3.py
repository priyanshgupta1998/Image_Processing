

import cv2
import numpy as np

img  = np.ones((512,512,3),np.uint8)
cv2.imshow('WINDOW',img)  # it will display a black image

cv2.imwrite('C:\\Users\\PRIYANSH\\Desktop\\datascience\\Opencv\\Output\proyog3.jpg',img)

cv2.waitKey(0)
cv2.destroyWindow('Priyansh') 
