import cv2

# Read the input image in grayscale mode
image = cv2.imread('./openCv/data/lena.jpg', 0)

# Set a threshold value (150 in this example)
threshold_value = 150

# Apply simple thresholding
_, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Display the original and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)

# Wait for a key event and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
