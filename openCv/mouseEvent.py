import cv2 as cv 
import numpy as np
import sys

sys.path.append("/media/HDD1/Courses/Python/openCv/opencv/samples/data")
pathimg = sys.path
print(pathimg)

# get list of event 
# events = [i for i in dir(cv) if "EVENT" in i]
# print(events)

def click_event(event, x, y, flages, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x," ", y)
        font = cv.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ", " + str(y)
        cv.putText(img, strXY, (x, y), font, 0.4, (255,255,0), 2)
        cv.imshow("image", img)
    if event == cv.EVENT_RBUTTONDOWN:
        #get channels from image
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ", " + str(green) + ", " + str(red)
        cv.putText(img, strXY, (x, y), font, 0.4, (0,255,255 ), 2)
        cv.imshow("image", img)

# img = np.zeros((512, 512, 3), np.uint8)
img = cv.imread(pathimg[7] + "/messi5.jpg")
cv.imshow("image", img)
cv.setMouseCallback("image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()