import cv2
import numpy as np
img = cv2.imread('Photos/mahoraga-jjk-4k-wallpaper.jpg')
img_resizeed = cv2.resize(img, (800,800))

cv2.imshow('Resized Image', img_resizeed)
cv2.waitKey(0)
cv2.destroyAllWindows()