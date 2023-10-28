import cv2 as cv
import numpy as np
import sys

img = cv.imread(sys.path[0] + "/opencv/samples/data/messi5.jpg", -1)
cv.imshow("Display Window", img)
k = cv.waitKey(0)

px = img[100,100]
print(px)

cv.destroyAllWindows()