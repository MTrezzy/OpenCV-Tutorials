import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read() # retval is not used here but shows if something wrong is happening

	width = int(cap.get(3)) # 3 == width (values by default are floating point)
	height = int(cap.get(4))# 4 == height

	image = np.zeros(frame.shape, np.uint8)
	smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

	image[:height//2, :width//2] = smaller_frame # Top left
	image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) # Bottom left
	image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) # Top right
	image[height//2:, width//2:] = smaller_frame # Bottom right

	cv2.imshow('frame', image)

	if cv2.waitKey(30) == ord('q'):
		break

cap.release() # release the camera resource
cv2.destroyAllWindows()