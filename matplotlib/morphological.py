import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./openCv/opencv/samples/data/smarties.png", cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

# apply whit square on ball
kernal = np.ones((5, 2), np.uint8)

#remove black dot from mask 
dilation =  cv.dilate(mask, kernal, iterations=2)

#remove black dot completely 
erosin = cv.erode(mask, kernal, iterations=2)

#remove black dot completely 
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)

#other morphological 
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal)

titles = ["image", "mask", "dilation", "erosion", "opening", "closing", "mg"]
image = [img, mask, dilation, erosin, opening, closing, mg]

for i in range(len(titles)):
    plt.subplot(2, 4, i+1), plt.imshow(image[i], "gray")
    plt.title(titles[i])    
    plt.xticks([]), plt.yticks([])


plt.tight_layout() 
plt.show()