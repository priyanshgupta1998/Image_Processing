import cv2
def main():
    img = cv2.imread("C:\\Users\\PRIYANSH\\Desktop\\Images\\home2.jpg")    #read the image
    #  img = cv2.imread("C:\\Users\\PRIYANSH\\Desktop\\Images\\home2.jpg" , 0)    # For read  the gray image # 2D image will be depicted     # 0-->Black #255---->White
    print(img.dtype)  # datatype of each item/element /number in the tuple
    print(img.shape) # resolution of the image   (height , width , no._of_channels)
    print(img.ndim)  # find_out the dimension of the image
    print(len(img))  # length of the image
    print(type(img))    # it will return 'numpy.ndarray'  which means N-dimentional array
    print(img.size)   # size of the image   (width*height)
    
if __name__ =="__main__":
    main()
