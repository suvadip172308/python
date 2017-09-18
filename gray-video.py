import numpy as np
import cv2

cap = cv2.VideoCapture('Wildlife.wmv')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    pressedKey = cv2.waitKey(600) & 0xFF;
    
    if pressedKey == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
