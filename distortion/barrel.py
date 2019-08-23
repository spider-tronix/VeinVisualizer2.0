import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
import time

np.set_printoptions(threshold=sys.maxsize)
tmatrix = np.load('tmat-new.npy') 

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
prog_start = time.time()

def process(frame):
		#frame_start = time.time()
		img = cv2.resize(frame,(256,256))
		img = np.fliplr(img)

		img_r = img.reshape((256*256, 3))
		res = np.zeros((256**2, 3), dtype=np.uint8)
		
		for i in tmatrix:
			res[i[0]] = img_r[i[1]-1]
		res = res.reshape((256, 256, 3))
		return(res)

while(ret):
	ret, frame = cap.read()
	res = process(frame)
	cv2.imshow('res', np.hstack((res,res)))	 
	if (cv2.waitKey(1) & 0xFF == ord('q')):
		break

cap.release()
cv2.destroyAllWindows()
