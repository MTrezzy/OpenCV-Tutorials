import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    # Change the BGR into an HSV image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # black out the pixels not in the range, otherwise change the pixel into white
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # apply the mask
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('frame', result)
    # We can also display the mask
    #cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()