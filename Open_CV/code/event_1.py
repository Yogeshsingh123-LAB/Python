import cv2
import numpy as np
def draw_circle(event, x, y, _flags, _param):
    if event == 1:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
cv2.namedWindow(winname='image')
cv2.setMouseCallback('image', draw_circle)
img = np.zeros((512, 512, 3), np.uint8)
while True:
    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()