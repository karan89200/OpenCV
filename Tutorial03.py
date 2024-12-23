import cv2
import numpy as np
#AIM : Extracting Blue , Green , Red channel separately and stacking them to see compare

img = cv2.imread("img/fruit.jpg")


# Extracting Images 
RedImg = img[:,:,0]
GreenImg = img[:,:,1]
BlueImg = img[:,:,2]



ImgStack = np.hstack((RedImg,GreenImg,BlueImg))


cv2.imshow("window",ImgStack)
cv2.waitKey(0)

