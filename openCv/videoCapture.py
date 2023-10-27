import numpy as np
import sys
import cv2 as cv

pathimg = sys.path

# set camera device for inbuilt use -1 or 0 and continues further devices 1,2..
# read from file then give file name instade of 0
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')

width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
print("Width  : ", width)
print("Height :" , height)
print(type(width))
out = cv.VideoWriter(pathimg[0] + "/output.avi", fourcc, 20.0, (1280, 720))

if not cap.isOpened():
    print("Can not open Camera")
    exit()

while True:
    #frame avialable then store true in ret and frame captured in frame variable 
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    else:
        out.write(frame)

         #gray variable show gray colore video
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
        #instade of gray use frame to show color video
        cv.imshow('frame', frame)
        
        if cv.waitKey(1) == ord('q'):
            break

cap.release()
out.release()
cv.destroyAllWindows()