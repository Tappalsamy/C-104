import cv2

img=cv2.imread("poster.jpg")
rocket=img[120:360,400:500]
img[0:240,500:600]=rocket

message="Hello world..."
cv2.putText(img,message,(20,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
cv2.imshow("Poster",img)
cv2.waitKey(0)