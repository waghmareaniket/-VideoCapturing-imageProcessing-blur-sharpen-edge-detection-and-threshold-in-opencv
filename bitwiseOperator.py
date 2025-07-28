import cv2
import numpy as np
img1=np.zeros((300,300),dtype='uint8')
img2=np.zeros((300,300),dtype='uint8')

cv2.circle(img1,(150,150),100,255,-1)
cv2.rectangle(img2,(250,250),(100,100),255,-1)

bitwise_and=cv2.bitwise_and(img1,img2)
bitwise_or=cv2.bitwise_or(img1,img2)
bitwise_not=cv2.bitwise_not(img1)

cv2.imshow('circle',img1)
cv2.imshow('rectangle',img2)
cv2.imshow('AND',bitwise_and)
cv2.imshow('OR',bitwise_or)
cv2.imshow('NOT',bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
