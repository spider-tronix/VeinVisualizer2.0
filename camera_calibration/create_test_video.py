import cv2
import numpy as np
import glob

img_array = []
size = None
for filename in glob.glob('assets/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    for _ in range(30):
        img_array.append(img)

out = cv2.VideoWriter('pic_slides.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()