import numpy as np;
import cv2;

# Actual image
img_actual = cv2.imread('ronaldo.jpg');
cv2.imshow('Ronaldo Colored', img_actual);
cv2.waitKey(3000);
cv2.destroyWindow('Ronaldo Colored');

img_gray = cv2.imread('ronaldo.jpg', 0);
cv2.imshow('Ronaldo Gray', img_gray);

# Resizable empty window and the load image into it
# introduce multiline comments

"""
cv2.namedWindow('Empty Image', cv2.WINDOW_NORMAL);
cv2.imshow('Empty Image', img_gray);
"""

# if 'ESC' pressed then window escaped and 's'
# pressed then save the image

keyPressed = cv2.waitKey(0);

if keyPressed == 27 or 13:
    cv2.destroyAllWindows();
elif keyPressed == ord('s'):
    cv2.imwrite('ronaldogray.jpeg', img_gray);
    cv2.destroyAllWindows();



