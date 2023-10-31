import cv2 as cv
import numpy as np
import sys

sys.path.append("/media/HDD1/Courses/Python/openCv/opencv/samples/data")
pathimg = sys.path

img = cv.imread(pathimg[7] + "/sudoku.png", 0)

# simple binary thresolding not work properly
_,th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# adaptive method 1
# 11 is block size of neihbourhood area
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

# adaptive method 2
# 11 is block size of neihbourhood area
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# cv.imshow("image", img)
# cv.imshow("th 1", th1)
cv.imshow("th 2", th2)
cv.imshow("th 3", th3)

cv.waitKey(0)