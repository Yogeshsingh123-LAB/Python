import cv2

img = cv2.imread('Photos/5151029.png')
if img is None:
    raise FileNotFoundError("Image not found: Photos/5151029.png")
#fliped_img = cv2.flip(img, 0)   #1 for horizontal flip, 0 for vertical flip, -1 for both
flipped_img = cv2.flip(img, 1)  # 1 for horizontal flip, 0 for vertical flip, -1 for both
#fliped_img = cv2.flip(img, -1)  # 1 for horizontal flip, 0 for vertical flip, -1 for both
cv2.imshow('Flipped Image', flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()