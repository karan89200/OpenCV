import cv2
import numpy as np
img = np.zeros((500,500,3))



# for demo ---------- below ----------
# def draw(event,x,y,flags,params):
#     # event : hover = 0, left-clickdown = 1 , left-clickrealse = 4, right-clickdown = 2, right-clickrelease = 5
#     print(event, " x :", x , " y :",y)
#     print(flags, params)

def draw(event,x,y,flags,params):
    if event == 1:
        cv2.circle(img,center=(x,y),radius=(30),thickness=-1,color=(0,0,255))


cv2.namedWindow(winname="windows")
cv2.setMouseCallback("windows",draw)


# code for continous dispalying window , Close = type 'x' from keyboard
while True:
    cv2.imshow("windows",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break



cv2.destroyAllWindows()