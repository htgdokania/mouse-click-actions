#['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON',
#'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN',
#'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP',
#'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK',
#'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

import cv2
import numpy as np
from math import sqrt

def calc_distance(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return round(sqrt((x1-x2)**2 + (y1-y2)**2))

# param contains the center and the color of the circle 
def draw_red_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        center = param[0]
        radius = calc_distance((x, y), center)
        cv2.circle(img, center, radius, param[1], 2)


def draw_blue_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        center = (300,300)
        radius = calc_distance((x, y), center)     
        cv2.circle(img, center, radius, (255, 0, 0), 2)

img = np.ones((600,600,3), np.uint8)
img.fill(255)

# create 2 windows
cv2.namedWindow("img_red")
cv2.namedWindow("img_blue")

# different doubleClick action for each window
# you can send center and color to draw_red_circle via param
param = [(300,300),(0,0,255)]
cv2.setMouseCallback("img_red", draw_red_circle, param)
cv2.setMouseCallback("img_blue", draw_blue_circle) # param = None


while True:
    # both windows are displaying the same img
    cv2.imshow("img_red", img)
    cv2.imshow("img_blue", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
