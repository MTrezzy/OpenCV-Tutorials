import cv2

img = cv2.imread('assets/img.png', cv2.IMREAD_COLOR)

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) 
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('assets/new_img.png', img)

cv2.imshow('My image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()