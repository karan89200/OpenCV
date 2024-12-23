import cv2

# Aim : Flipping the image both vertically and horizontally

# image reading

img = cv2.imread("img/fruit.jpg")

vImg = cv2.flip(img,0) # vertical flipping
hImg = cv2.flip(img,1) # horizontal flipping
VerticalAndHorizontal = cv2.flip(img,-1) # vertical and horizontal flipping
cv2.imshow("Original",img)
cv2.imshow("Vertical",vImg)
cv2.imshow("Horizontal",hImg)
cv2.imshow("Vertical and Horzontal",VerticalAndHorizontal)

cv2.waitKey(0)