import cv2 as cv
import numpy as np 
import sys

sys.path.append("/media/HDD1/Courses/Python/openCv/opencv/samples/data")
pathimg = sys.path

def nothing(x):
    pass
cv.namedWindow("trackBar")
cv.createTrackbar("LH", "trackBar", 0, 255, nothing)
cv.createTrackbar("LS", "trackBar", 0, 255, nothing)
cv.createTrackbar("LV", "trackBar", 0, 255, nothing)
cv.createTrackbar("UH", "trackBar", 255, 255, nothing)
cv.createTrackbar("US", "trackBar", 255, 255, nothing)
cv.createTrackbar("UV", "trackBar", 255, 255, nothing)

while True:
    img = cv.imread(pathimg[7] + "/smarties.png")

    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV) # grey image

    l_h =cv.getTrackbarPos("LH", "trackBar")
    l_s =cv.getTrackbarPos("LS", "trackBar")
    l_v =cv.getTrackbarPos("LV", "trackBar")

    u_h =cv.getTrackbarPos("UH", "trackBar")
    u_s =cv.getTrackbarPos("US", "trackBar")
    u_v =cv.getTrackbarPos("UV", "trackBar")
    
    l_b = np.array([l_h, l_s, l_v]) # find rang using trackbar
    u_b = np.array([u_h, u_s, u_v])

    mask = cv.inRange(hsv, l_b, u_b) # mask image 
    res = cv.bitwise_and(img, img, mask=mask)

    cv.imshow("frame", img)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    k = cv.waitKey(0)

    if k == 27:
        break

cv.destoryAllWindows()