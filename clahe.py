import numpy as np
import cv2

kernel7 = np.ones((7,7), np.uint8)
kernel3 = np.ones((3,3), np.uint8)

def multi_clahe(img, num):
    for i in xrange(num):
	    img = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4+i*2,4+i*2)).apply(img)
    return img

fname = '1.png'

img = cv2.imread(fname)
hsv = gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv_thresh = cv2.inRange(hsv, (0, 0, 45), (180, 255, 255))

org = np.copy(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_and(gray, hsv_thresh, gray)

# bilateral takes more time
blur = cv2.bilateralFilter(gray,9,75,75)
#blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_CONSTANT)

mclahe = multi_clahe(blur, 4)

cv2.imshow('original',org)
cv2.imshow('clahe',mclahe)
cv2.imwrite(fname.strip('.png')+ 'clahe.png', mclahe)

#ret3,th3 = cv2.threshold(final,0,255,cv2.THRESH_OTSU)
#cv2.imshow('otsu',th3)

x = (mclahe < 50)
x = np.array(x, dtype=np.uint8)*255
cv2.line(x, (x.shape[0]/2, 0), (x.shape[0]/2, x.shape[1]), 128, 1)
cv2.line(x, (0, x.shape[1]/2), (x.shape[0], x.shape[1]/2), 128, 1)
cv2.imshow('mask of clahe',x)
cv2.imwrite(fname.strip('.png')+ 'mask.png', x)

cv2.waitKey(0)
cv2.destroyAllWindows()
