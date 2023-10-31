from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import sys

pathimg = sys.path

#using pillow only
with Image.open("./matplotlib/stinkbug.png") as im:
    im.show()

# using pillow and plot using matplotlib
img = np.asarray(Image.open('./matplotlib/stinkbug.png'))
imgplot = plt.imshow(img) # plot image so use plt 
plt.show()
# print(repr(img))

#using opencv open image and plot using mat plotlib
img = cv.imread("./openCv/lena.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB) # if conver into color image then
plt.imshow(img)
plt.xticks([]), plt.yticks([]) # hide scale in ploting image
plt.show()

# Image.open statement is same the only diffrence is
# secons method use variable and first one is while loop