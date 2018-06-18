import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(0,255,0),-1)

#"""test mouse callback function
def draw_circle1(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(0,200,200),3)
#"""
        
# Create a white image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
img.fill(255)
cv2.namedWindow('image')
cv2.namedWindow('image1')
cv2.setMouseCallback('image',draw_circle)
cv2.setMouseCallback('image1',draw_circle1)

while(1):
    cv2.imshow('image3',img)
    cv2.imshow('image',img)
    cv2.imshow('image1',img)
    if cv2.waitKey(20) & 0xFF ==ord('q'):
        break

cv2.destroyAllWindows()
