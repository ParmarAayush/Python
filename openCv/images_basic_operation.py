import cv2 as cv

#load image from file source 
image = cv.imread("./openCv/data/lena.jpg")

# Convert image to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Load the pre-trained face detection classifier from OpenCV
face_cascade = cv.CascadeClassifier('./openCv/Algorithms/haarcascade_frontalface_default.xml')

# Perform face detection
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

ret, thresholded_image = cv.threshold(gray_image, 127, 255, cv.THRESH_BINARY)

# Set a threshold value (150 in this example)
threshold_value = 150

# Apply simple thresholding
_, thresholded_image = cv.threshold(gray_image, threshold_value, 255, cv.THRESH_BINARY)

cv.imshow('Original Image', image)
cv.imshow('Thresholded Image', thresholded_image)

cv.imshow("Image", gray_image)
cv.waitKey(0)