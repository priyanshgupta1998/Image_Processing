# Edge Detection and gradients
import cv2
import numpy as np

cap = cv2.VideoCapture(0)   # select the first camera in the system

while True:
    _ , frame = cap.read()   

    laplacian = cv2.Laplacian(frame,cv2.CV_8U)

    #see the intensity of the noises and error.
    sobelx = cv2.Sobel(frame ,cv2.CV_8U, 1,0 ,ksize =5)
    sobely = cv2.Sobel(frame , cv2.CV_8U , 0,1,ksize =5)


    # for Edge Detection we use Canny() method 
    edges = cv2.Canny(frame , 100,100)
    

    cv2.imshow('Original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('edges_detection',edges)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
    




    

