import cv2

img = cv2.imread('Photos/mahoraga-jjk-4k-wallpaper.jpg')
img_cropped = img[0:200, 200:500]
cv2.imwrite('Photos/mahoraga-jjk-4k-wallpaper-cropped.jpg', img_cropped)
cv2.waitKey(0)
