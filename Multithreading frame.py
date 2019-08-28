import cv2
import numpy as np 
from threading import Thread
import queue
clahe_count=20
relay_count=50
kernel7 = np.ones((7,7), np.uint8)
kernel3 = np.ones((3,3), np.uint8)
my_q = queue.Queue()
my_q1 = queue.Queue()
cap=cv2.VideoCapture(0)
count=1

def multi_clahe(img, num):
    for i in range(num):
	    img = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4+i*2,4+i*2)).apply(img)
    my_q.put(img)
def image_process(img,hsv_thresh):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.bitwise_and(gray, hsv_thresh, gray)
	blur = cv2.bilateralFilter(gray,9,75,75)
	my_q1.put(blur)	

if __name__ == '__main__':
	while(1):
		ret,img=cap.read()
		cv2.imshow("video_relay",img)
		org = np.copy(img)
		if(count<=clahe_count):	
			hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			hsv_thresh = cv2.inRange(hsv, (0, 0, 45), (180, 255, 255))
			t1=Thread(target=image_process,args=(img,hsv_thresh))
			t1.start()
			#t1.join()
			blur=my_q1.get()
			t = Thread(target=multi_clahe,args=(blur,4))
			t.start()
			#t.join()
			clahe=my_q.get()
		cv2.imshow("clahe",clahe)
		reoo = cv2.cvtColor(clahe, cv2.COLOR_GRAY2BGR)
		vin=cv2.addWeighted(reoo, 0.55, org, 0.95, 0)
		cv2.imshow("coloursuper",vin)
		key=cv2.waitKey(2)
		count=count+1
		if(count>=relay_count):
			count=1
		if(key==ord('s')):
			count=2
			cap.release()
			cv2.destroyAllWindows()
			break
        




