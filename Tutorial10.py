import cv2
import numpy as np

img = np.zeros((500,700,3))

flag = True
ix = -1
iy = -1
def draw(event,x,y,flags,params):

    global flag,ix,iy
    if event == 1:
        flag = False
        ix = x
        iy = y
    elif event == 0:
        if flag == False:
            # cv2.circle(img,center=(x,y),radius=10,color=(0,0,255),thickness=-1)
            cv2.line(img, (ix, iy), (x, y), (0, 0, 255), thickness=2)
            ix, iy = x, y  # Update the starting point for the next line segment
            # cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,255),thickness=-1)
    elif event == 4:
        flag = True
        # cv2.circle(img,center=(x,y),radius=10,color=(0,0,255),thickness=-1)
        # cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,255),thickness=-1)
        cv2.line(img, (ix, iy), (x, y), (0, 0, 255), thickness=2)
    

cv2.namedWindow(winname='window')
cv2.setMouseCallback("window",draw)

while True:

    cv2.imshow("window",img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
    
    
