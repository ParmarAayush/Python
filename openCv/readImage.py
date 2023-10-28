import cv2 as cv
import sys

# if you want to add path manually which use further
sys.path.append("/media/HDD1/Courses/Python/openCv/opencv/samples/data")
print(sys.path)
pathimg = sys.path

# direct read from sample folder in opencv 
# img = cv.imread(cv.samples.findFile("lena.jpg"))

# also read using direct path
# img = cv.imread("/media/HDD1/Courses/openCv/opencv/samples/data/lena.jpg", -1)

img = cv.imread(pathimg[7] + "/lena.jpg", -1) # set sys path when required multiple path and use 

if img is None:
    print(img)
    sys.exit("Could Not Found Image.")

cv.imshow("Display Window", img) # show and close window use waitKey
k = cv.waitKey(0) # close window when press key 

# write file 
if k == ord("s"):
    print(pathimg[0])
    cv.imwrite( pathimg[0] + "/starry_night.png", img)