import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append("/media/HDD1/Courses/Python/openCv/opencv/samples/data")
pathimg = sys.path

img = cv.imread(pathimg[7] + "/gradient.png", 0)

_,th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_,th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_,th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

# code from thresolding.py now combine into one display
# cv.imshow("image", img)
# cv.imshow("thresold 1", th1)
# cv.imshow("thresold 2", th2)
# cv.imshow("thresold 3", th3)

total = ["image", "thresold 1", "thresold 2", "thresold 3"]
images = [img, th1, th2, th3]
print(len(total))
for i in range(len(total)):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], "gray")
    plt.title(total[i])

plt.tight_layout()  # Add this line to adjust subplot spacing
plt.show()
cv.waitKey(0)
