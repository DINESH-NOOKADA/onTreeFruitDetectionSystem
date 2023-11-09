import cv2
import numpy as np

# Load the binary image
img = cv2.imread('Area4.png', 0)

# Define the kernel for erosion
kernel = np.ones((30, 30), np.uint8)

# Apply the erosion operation
img_eroded = cv2.erode(img, kernel, iterations=1)

# Count the number of mangoes in the eroded image
# num_mangoes, labels = cv2.connectedComponents(img_eroded)

# Print the number of mangoes
# print('Number of mangoes:', num_mangoes - 1)

# Save the eroded image
cv2.imwrite('erodedImage4.png', img_eroded)