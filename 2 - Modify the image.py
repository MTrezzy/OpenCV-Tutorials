import cv2
import random

img = cv2.imread('../assets/img.png', cv2.IMREAD_COLOR)

print(img)
print("Type:", type(img))
print("Shape:", img.shape)

for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

tag = img[150:200, 70:100]
img[0:50, 150:180] = tag

cv2.imshow('Image with random values', img)
cv2.waitKey()
cv2.destroyAllWindows()


