import cv2

img = cv2.imread('Photos/me.jpg')
img_cropped = img[0:200, 200:500]
cv2.imshow('Cropped Image', img_cropped)
cv2.waitKey(0)