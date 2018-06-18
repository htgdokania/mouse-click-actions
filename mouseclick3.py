import cv2
import time as t
import numpy as np
img = np.zeros([600,600],np.uint8)
img.fill(0) # it fills the entire image with white pixels
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
