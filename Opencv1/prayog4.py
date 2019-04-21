# with the TRACKBAR gui component
# we can perform some action my moving cursor
import cv2
import numpy  as np

def funk():      # create one funciton # Now we are not  adding any action in it . # just  pass
    pass

def main():
    img1 = np.zeros((512,512,3) , np.uint8)   # create a imgae of size 512 x512
    windowName = 'openCV BGR color Palette'   # give the name to window which will appear after the execution ofthis program 
    cv2.namedWindow(windowName)   # putting it (name) into the command


    # create just labels
    # make a Trackbar (we can scroll and change the color manually  upto range 0 -255)
    # just create scroll label
    cv2.createTrackbar('B',windowName , 0 , 255 , funk)   
    cv2.createTrackbar('G',windowName , 0 , 255 , funk)
    cv2.createTrackbar('R',windowName , 0 , 255 , funk)

    while(True):
        cv2.imshow(windowName , img1)  # display the image on the window which we have created earlier
        #exit from the loop
        if cv2.waitKey(20)>0:   # enter  the any key  to close the window
            break

        # put/ decide the colors on the labels corresponding windowNmae
        # when scroll will move then  track position will also be changed ., so corresponding to that position these below commands will perform some action
        blue = cv2.getTrackbarPos('B' , windowName)      
        green = cv2.getTrackbarPos('R' , windowName)
        red = cv2. getTrackbarPos('G' , windowName)

        img1[:]= [blue ,green , red]   #  correspoding to cordinates this image will be shown
        print(blue , green , red)
         
    cv2.destroyAllWindows()

    
if __name__ == "__main__":
    main()

