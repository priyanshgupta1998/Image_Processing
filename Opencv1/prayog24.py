# Extract the foreground image

import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread("C:\\Users\\PRIYANSH\\Desktop\\Images\\me.jpg")


mask = np.zeros(img.shape[:2] , np.uint8)

bgd_model = np.zeros((1,65) , np.float64)   # 2d array 
fgd_model = np.zeros((1,65) , np.float64)    # 2d array


rect = (260,40,150,180)  #rect = (start_x, start_y, width, height).

cv2.grabCut(img,mask,rect,bgd_model,fgd_model,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()



















































