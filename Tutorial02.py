import  cv2

#Aim: Converting an RGB image to GrayScale image


img = cv2.imread("img/fruit.jpg") #reading an image

#converting RGB to grayscale
grayScaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#displaying both
cv2.imshow("window1",img)
cv2.imshow("window2",grayScaled_img)

cv2.waitKey(0)