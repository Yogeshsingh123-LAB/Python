import cv2
import time 

cap = cv2.VideoCapture('output.avi')

while True:
    ret, frame = cap.read()
    time.sleep(1/20)  # Adjust the sleep time based on the desired frame rate
   
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()