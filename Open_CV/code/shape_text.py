import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
#Rectangle
cv2.rectangle(img, pt1=(100, 100), pt2=(300, 300), color=(0, 255, 0), thickness=2)
#thickness = -1 will fill the rectangle with color
#circle
cv2.circle(img, center=(400, 50), radius=30, color=(255, 0, 0), thickness=3)

#line
cv2.line(img, pt1=(0,0), pt2=(100,100), color=(0, 0, 255), thickness=5, lineType=cv2.LINE_AA)

#Text
cv2.putText(img, "Hello", org=(10, 50), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

cv2.imshow('Image', img)
cv2.waitKey(0)