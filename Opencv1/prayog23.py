
#Template Matching
# find one image in another image 

import cv2
import numpy as np

img_rgb = cv2.imread('C:\\Users\\PRIYANSH\\Desktop\\Images\\opencv-template-matching-python-tutorial.jpg')


img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)   # Gray color image
#cv2.imshow('img_gray',img_gray)


template = cv2.imread('C:\\Users\\PRIYANSH\\Desktop\\Images\\opencv-template-for-matching.jpg',0)
w, h = template.shape[::-1]   # just reverse  rows <--> column  or X <---->Y    


#Now match the template 
res = cv2.matchTemplate(img_gray,template,  cv2.TM_CCOEFF_NORMED)

threshold = 0.8# make a gate  # decide a entry value 

loc = np.where( res >= threshold)
#  *loc[::-1]  # make a marticx for m

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb ,  pt,  (pt[0] + w ,  pt[1] + h)  , (0,0,255), 1)   # here 'pt' is cordinate from matrix array
   # print(pt)


cv2.imshow('Detected',img_rgb)


