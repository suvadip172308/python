import numpy as np;
import cv2;

# Actual image
img_actual = cv2.imread('ronaldo.jpg');
cv2.imshow('Ronaldo Clored', img_actual);

img_gray = cv2.imread('ronaldo.jpg', 0);
cv2.imshow('Ronaldo Gray', img_gray);
cv2.waitKey(5000);
cv2.destroyAllWindows();