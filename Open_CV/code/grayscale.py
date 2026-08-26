import cv2

img = cv2.imread("Photos/me.jpg")
if img is None:
	raise FileNotFoundError("Could not read Photos/me.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

if not cv2.imwrite("Photos/me_grayscale.jpg", gray):
	raise IOError("Could not save Photos/me_grayscale.jpg")

cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

