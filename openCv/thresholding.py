import cv2 as cv
import numpy as np
import sys

sys.path.append("/media/HDD1/Courses/Python/openCv/opencv/samples/data")
pathimg = sys.path

img = cv.imread(pathimg[7] + "/gradient.png", 0)

# if px is lesthen 127 the value is zero(0) black and grater then value 255 
_,th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# invert binary result
_,th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
# pixal value unchande lessthan 127 and if greater then it change as 127 
_,th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)



cv.imshow("image", img)
cv.imshow("thresold 1", th1)
cv.imshow("thresold 2", th2)
cv.imshow("thresold 3", th3)

cv.waitKey(0)