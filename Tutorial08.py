import numpy as np
import cv2

# Aim : Create a Rectange, Circle, Line and Text

#create a black screen for creating shapes on it.
box = np.zeros((500,500,3))

cv2.rectangle(box,pt1 = (50,50), pt2 = (300,200),color=(0,33,34),thickness=3)
cv2.circle(box,center=(400,130),radius= 70,color=(23,234,123),thickness=3)
cv2.line(box,pt1=(50,250),pt2=(400,250),color=(22,22,22),thickness=10)
cv2.putText(box,text="KARAN",fontScale= 4,color = (46,78,119),org=(50,400),fontFace=cv2.FONT_HERSHEY_COMPLEX)
cv2.imshow("windos",box)
cv2.waitKey(0)