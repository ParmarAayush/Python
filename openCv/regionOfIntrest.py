import cv2 as cv
import numpy as np
import sys

#ROI : region of intrest is particular area of an image 
#Example : massi kick football then if we select football
#        : Logo in particular image 
sys.path.append("/media/HDD1/Courses/Python/openCv/opencv/samples/data")
print(sys.path)
pathimg = sys.path

img = cv.imread(pathimg[7] + "/messi5.jpg")

print(img.shape) # return tuple, number of rows, columns, channels
print(img.size) # total number of pixels accessed
print(img.dtype) # obtained image dataType

b,g,r = cv.split(img)
img = cv.merge((b,g,r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball # how to measure proper co-ordinates tutorial 8-9

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
