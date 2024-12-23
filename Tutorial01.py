
import numpy as np
import cv2

img = cv2.imread('img/fruit.jpg')
print(img.shape)

cv2.imshow('window',img)
cv2.waitKey(0)