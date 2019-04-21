import cv2
def main():
    img = cv2.imread("C:\\Users\\PRIYANSH\\Desktop\\Images\\home2.jpg")    #read the image
    #  img = cv2.imread("C:\\Users\\PRIYANSH\\Desktop\\Images\\home2.jpg" , 0)    # For read  the gray image 
    cv2.imshow('Priyansh',img)      # display the image on the screen
    cv2.imwrite('C:\\Users\\PRIYANSH\\Desktop\\datascience\\Opencv\\Output\proyog0.jpg',img)   # save the image file in the output folder
    cv2.waitKey(0)   #it is combine with the keyboard event , it won't execute / cancel until we press any key .  basically it will wait for the infinite time.
    cv2.destroyWindow('Priyansh')   # close /detroy the window

if __name__ =="__main__":
    main()
