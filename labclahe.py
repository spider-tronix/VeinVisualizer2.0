import cv2

img = cv2.imread('1.png')
cv2.imshow("img",img) 
blur = cv2.bilateralFilter(img,9,75,75)
lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#cv2.imshow("lab",lab)

l, a, b = cv2.split(lab)
#cv2.imshow('l_channel', l)
#cv2.imshow('a_channel', a)
#cv2.imshow('b_channel', b)

clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
cl = clahe.apply(l)
#cv2.imshow('CLAHE output', cl)

limg = cv2.merge((cl,a,b))
#cv2.imshow('limg', limg)

final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
cv2.imshow('final', final)
cv2.imwrite('labclahe-1.png', final)
cv2.waitKey(0)
