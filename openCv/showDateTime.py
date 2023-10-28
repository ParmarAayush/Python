import numpy as np
import sys
import cv2 as cv
import datetime

pathimg = sys.path

# set camera device for inbuilt use -1 or 0 and continues further devices 1,2..
# read from file then give file name instade of 0
cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter(pathimg[0] + "/output.avi", fourcc, 20.0, (1280, 720))

while (cap.isOpened()):
    #frame avialable then store true in ret and frame captured in frame variable 
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    else:
        font = cv.FONT_HERSHEY_SIMPLEX
        text = "Width :" + str(cap.get(3)) + "Height :" + str(cap.get(4))
        datet = str(datetime.datetime.now())
        #frame = cv.putText(frame,text, cordinates(x,y), font, fontScale, color, thickness, Line type)
        frame = cv.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv.LINE_AA)

        out.write(frame)
        #instade of gray use frame to show color video
        cv.imshow('frame', frame)
        
        if cv.waitKey(1) == ord('q'):
            break

cap.release()
out.release()
cv.destroyAllWindows()