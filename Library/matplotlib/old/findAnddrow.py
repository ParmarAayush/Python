import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("/media/HDD1/Courses/Python/openCv/opencv/samples/data/opencv-logo.png")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh =  cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

print("Number of contours:", len(contours))

cv.drawContours(img, contours, 15, (0, 255, 0), 5)

cv.imshow("image", img)
cv.imshow("image Gray", imgray)
cv.waitKey(0)
