import cv2
import numpy as np
flag = False
ix =-1
iy=-1
def crop(event, x, y, flags, param):
    global ix, iy, flag
    if event  == 1:
        flag = True
        ix, iy = x, y
    # elif event ==0:
    #     if flag == True:
    #         cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 0), 2)
    elif event == 4:
        fx = x
        fy = y
        flag = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 0), 2)
        #ceop tool
        cropped = img[iy:fy, ix:fx]
        cv2.imshow('Cropped', cropped)
        cv2.imwrite('Photos/cropped.jpg', cropped)
        cv2.waitKey(0)
img = cv2.imread('Photos/me.jpg')
cv2.namedWindow(winname='Image')
cv2.setMouseCallback('Image', crop)

while True:
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyWindow('Image')