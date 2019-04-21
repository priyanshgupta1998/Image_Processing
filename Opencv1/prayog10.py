# we are using webcam .
# Save the output caputure vedio in the system.
import cv2
import numpy as np

img = cv2.imread( "C:\\Users\\PRIYANSH\\Desktop\\Images\\cat.jpg" , cv2.IMREAD_COLOR)   # colored image



#Draw a line 
cv2.line(img , (0,0) , (150,150),(255,255,255),15)

#Draw a rectangle
cv2.rectangle(img , (15,15) ,(200,150) ,(0,255,0) , 5)

# Draw a circle
cv2.circle(img , (400,300) , 70 , (0,214,98),1)   # grren circle
cv2.circle(img , (600,400) , 70 , (0,14,98),-1)   # brown  solid circle



# Draw a polygon
pts = np.array([[10,5] , [20,30] ,[58,94] , [69 ,57],[87,34]], np.int32)  # draw a polygon of combining 5 cordinates
cv2.polylines(img , [pts],True , (0,148,247) , 5)    # here 5 is the thickness of the line

# write the text on the image

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img , ' First Text ' , (100,550), font , 4, (200,255,125) ,5,cv2.LINE_AA)   # 5 is the thickness ofthe text and #  4 is the size of the text


cv2.imshow('Cat_image',img)
cv2.waitKey(0)    # wait for the user (for infinite time) to press the EXIT /ESC key to close the window  
cv2.destroyAllWindows()   # close all the windows 
