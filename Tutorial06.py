import cv2

# Aim : Cropping the image

img = cv2.imread("img/fruit.jpg")


CropImg = img[100:300, 200:400] # slicing image : height x width
cv2.imshow("cropped image",CropImg)
cv2.waitKey(0)