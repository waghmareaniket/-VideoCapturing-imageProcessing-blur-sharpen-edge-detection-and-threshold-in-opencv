import cv2
image=cv2.imread('blurImg.png')

blurred=cv2.GaussianBlur(image,(3,3),0)
cv2.imshow('originImg',image)
cv2.imshow('blurImg',blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()