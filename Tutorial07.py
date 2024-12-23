import cv2

# Aim : Save the image

# Reading the image
img = cv2.imread('img/fruit.jpg')

FlipImg = cv2.flip(img,0)
GrayScaledImage = cv2.cvtColor(FlipImg,cv2.COLOR_BGR2GRAY)

# save the img in png format
cv2.imwrite("img/TransformedImage.png",GrayScaledImage)