import cv2

img=cv2.imread("butterfly.jpg")
greyimg=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY )
cv2.imshow("Butterfly",greyimg)
cv2.waitKey(0)