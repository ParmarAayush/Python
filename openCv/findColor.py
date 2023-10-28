import cv2 as cv
import numpy as np
import sys

sys.path.append("/media/HDD1/Courses/Python/openCv/opencv/samples/data")
pathimg = sys.path

def click_event(event, x, y, flages, param):

    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv.circle(img, (x, y), 3, (0, 0, 225), -1)
        mycolorImg = np.zeros((512, 512, 3), np.uint8)

        mycolorImg[:] = [blue, green, red]
        cv.imshow("color", mycolorImg)

img = cv.imread(pathimg[7] + "/lena.jpg")
cv.imshow("image", img)
cv.setMouseCallback("image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()