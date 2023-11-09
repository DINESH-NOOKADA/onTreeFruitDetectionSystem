import cv2
import numpy as np

img = cv2.imread('binaryImage4.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = np.uint8(img_gray)
mask = np.zeros(img.shape[:2], dtype=np.uint8)  # Match the size of the image

cont, _ = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

count = 0
areac = 0

for i in range(len(cont)):
    area = cv2.contourArea(cont[i])
    if area != 0:
        areac += area
        count += 1

threshold_area = areac / count  # Threshold for contour area

for i in range(len(cont)):
    x, y, w, h = cv2.boundingRect(cont[i])
    area = cv2.contourArea(cont[i])
    if area > threshold_area:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        mask_roi = mask[y:y+h, x:x+w]
        mask_roi[:] = 255

# 

# Make sure the mask and image have the same size
if mask.shape[:2] != img.shape[:2]:
    mask = cv2.resize(mask, (img.shape[1], img.shape[0]))

result = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite('contourImgArea4.png', result)
cv2.imshow('Result', result)
# cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
