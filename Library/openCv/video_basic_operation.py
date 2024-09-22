import cv2 as cv

cap = cv.VideoCapture(0)  # 0 corresponds to the default camera

while True:
    ret, frame = cap.read()
    # Perform image processing on the frame
    # Display the processed frame
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
