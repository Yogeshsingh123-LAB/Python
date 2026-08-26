import cv2
import numpy as np
img = cv2.imread('Photos/mahoraga-jjk-4k-wallpaper.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_Blue = img[:,:,0]
img_Green = img[:,:,1]
img_Red = img[:,:,2]

new_img = np.hstack((img_Blue, img_Green, img_Red))
cv2.imshow('New Image', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()