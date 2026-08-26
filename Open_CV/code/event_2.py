import cv2
import numpy as np

flag = False
ix = -1
iy = -1
def draw_circle(event, x, y, flags, param):
    global ix, iy, flag
    if event == 1:
        flag = True
        ix, iy = x, y
    elif event == 0:
        if flag == True:
            cv2.rectangle(img, pt1=(ix,iy), pt2=(x,y), color=(0,225,255), thickness=-1)
    elif event == 4:
        flag = False
        cv2.rectangle(img, pt1=(ix,iy), pt2=(x,y), color=(0,225,255), thickness=-1)

cv2.namedWindow(winname='image')
cv2.setMouseCallback('image', draw_circle)
img = np.zeros((512, 512, 3), np.uint8)
while True:
    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()