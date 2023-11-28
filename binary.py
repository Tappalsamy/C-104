import cv2
import numpy as np

img=np.zeros([600,600])
img[200:400,200:400]=255
cv2.imshow("Black Image",img)
cv2.waitKey(0)