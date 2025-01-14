import numpy as np
import cv2

color = [255, 0, 0]
pixel = np.uint8([[color]])
# print(pixel)
hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
hsv = hsv[0][0]

print('BGR:', color)
print('HSV:', hsv)

img_color = cv2.imread('./image/circle_HSV_color.jpg', cv2.IMREAD_UNCHANGED)
height, width = img_color.shape[:2]

img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

lower_blue = (120-10, 30, 30)
upper_blue = (120+10, 255, 255)
img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask)

cv2.imshow('img_color', img_color)
cv2.imshow('img_mask', img_mask)
cv2.imshow('img_result', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()