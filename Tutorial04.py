import cv2

# Aim : Resize the image
img = cv2.imread("img/fruit.jpg")


# orginal size
cv2.imshow("window1",img)
# custom size 
ResizedImg = cv2.resize(img,(600,300))
cv2.imshow("window2",ResizedImg)

cv2.waitKey(0)