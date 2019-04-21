#Draw an image using numpy library


import cv2
import numpy as np

img  = np.zeros((512,512,3),np.uint8)   # width,height ,no_of_channels


# Now  i will draw something in the image
cv2.line(img,(0,153),(89,35) , (0,0,255) ,2)  # BGR order


#Draw a renctangle  
cv2.rectangle(img , (40,90) ,(120,130) ,(0,255,0) ,2)

#Draw a circle
# here center (60,60) ,
#radius = 50
cv2.circle(img , (60,60) ,50,(255,0,0) , -1)

#Draw a ellipse
'''
HERE center = (160,260)
major axis = 50
minor axis = 20
take the part of area = 360 (complete)
x_rotation =0  , y_rotaion = 0
'''
cv2.ellipse(img ,(160,260) ,(50,20), 0,0,360 ,(127,127,127) ,-1) 



points = np.array ([[80,2] , [125,0],[179,0],[230,5],[30,50]] , np.int32)
points = points.reshape((-1,1,2))
cv2.polylines(img , [points] ,True , (0,255,255))

text1 = 'Test Text '
cv2.putText(img , text1  , (100 ,100) , cv2.FONT_HERSHEY_SIMPLEX , 5 ,(255,255,0))

cv2.imshow('WINDOW',img)  # it will display a black image



cv2.imwrite('C:\\Users\\PRIYANSH\\Desktop\\datascience\\Opencv\\Output\proyog2.jpg',img)

cv2.waitKey(0)
cv2.destroyWindow('WINDOW') 
