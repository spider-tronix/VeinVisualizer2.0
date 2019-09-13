import numpy as np
import cv2
import pickle
import time


# Allows (+-)0.1 on dst[0] and dst[1]
# Allows (+-)0.01 on dst[4]

def nothing(x):
    pass


def ndtotext(A, w=None, h=None):
    if A.ndim == 1:
        if w == None:
            return str(A)
        else:
            s = '[' + ' ' * (max(w[-1], len(str(A[0]))) - len(str(A[0]))) + str(A[0])
            for i, AA in enumerate(A[1:]):
                s += ' ' * (max(w[i], len(str(AA))) - len(str(AA)) + 1) + str(AA)
            s += '] '
    elif A.ndim == 2:
        w1 = [max([len(str(s)) for s in A[:, i]]) for i in range(A.shape[1])]
        w0 = sum(w1) + len(w1) + 1
        s = u'\u250c' + u'\u2500' * w0 + u'\u2510' + '\n'
        for AA in A:
            s += ' ' + ndtotext(AA, w=w1) + '\n'
        s += u'\u2514' + u'\u2500' * w0 + u'\u2518'
    elif A.ndim == 3:
        h = A.shape[1]
        s1 = u'\u250c' + '\n' + (u'\u2502' + '\n') * h + u'\u2514' + '\n'
        s2 = u'\u2510' + '\n' + (u'\u2502' + '\n') * h + u'\u2518' + '\n'
        strings = [ndtotext(a) + '\n' for a in A]
        strings.append(s2)
        strings.insert(0, s1)
        s = '\n'.join(''.join(pair) for pair in zip(*map(str.splitlines, strings)))
    return s


with open("data.pickle", "rb") as handler:
    [objpoints, imgpoints] = pickle.load(handler)

frame = None
video_path = input("Enter path of video")
cap = cv2.VideoCapture(video_path)
count = 0
while cap.isOpened():
    _, frame = cap.read()
    count += 1
    if count == 5:  # Taking the 5th frame of the video for initial values
        break
cap.release()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

cv2.namedWindow('Bars')
cv2.createTrackbar('k1', 'Bars', 1000, 2000, nothing)
cv2.createTrackbar('k2', 'Bars', 1000, 2000, nothing)
cv2.createTrackbar('k3', 'Bars', 1000, 2000, nothing)


cap = cv2.VideoCapture(input("Enter path of video"))
count = 0
while cap.isOpened():
    _, frame = cap.read()
    count += 1
    if count == 5:  # Taking the 5th frame of the video for initial values
        break
cap.release()
    k1 = dist[0, 0] - 0.1 + cv2.getTrackbarPos('k1', 'Bars') / 10000.0
    k2 = dist[0, 1] - 0.1 + cv2.getTrackbarPos('k2', 'Bars') / 10000.0
    k3 = dist[0, 4] - 0.01 + cv2.getTrackbarPos('k3', 'Bars') / 100000.0

    new_dist = np.array([[k1, k2, dist[2], dist[3], k3]],
                        dtype=np.float)

    h, w = img.shape[:2]

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(new_mtx, new_dist, (w, h), 1, (w, h))

    # undistort
    dst = cv2.undistort(img, new_mtx, new_dist, None, newcameramtx)

    # crop the image
    x, y, w, h = roi
    dst = dst[y:y + h, x:x + w]

    cv2.imshow('calibrated', dst)
    cv2.imshow('original', gray)

    mean_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], new_mtx, new_dist)
        error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
        mean_error += error

    print(f"Current Total Error: {mean_error / len(objpoints)}"
          f"\nCurrent Camera Matrix : \n {ndtotext(new_mtx)}"
          f"\nCurrent Dist Matrix : \n {ndtotext(new_dist)}")
    time.sleep(0.1)

cv2.destroyAllWindows()
