import numpy as np
import cv2 as cv

img = cv.imread('lena.jpg', 1)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv.circle(img,(447,63), 63, (0,0,255), -1)



cv.imshow('Draw Shape', img)

k = cv.waitKey(0)
if k == ord("q"):
    print("closed image window")
