import cv2
import numpy as np

img=cv2.imread('lena.jpg')

cv2.startWindowThread()
cv2.namedWindow('image')

def f(x):
    return x

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,f)
cv2.createTrackbar('G','image',0,255,f)
cv2.createTrackbar('B','image',0,255,f)

while(1):
    
    cv2.imshow('image',img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')

cv2.destroyAllWindows()
