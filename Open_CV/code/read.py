import cv2 as cv

img = cv.imread("Photos/me.jpg")

if img is None:
    print("Image not found!")
else:
    cv.imshow("me", img)
    cv.waitKey(0)