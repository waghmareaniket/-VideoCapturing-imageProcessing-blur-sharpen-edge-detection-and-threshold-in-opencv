import cv2
image=cv2.imread('blurImg.png')
blurred=cv2.medianBlur(image,5)
cv2.imshow('originalmg',image)
cv2.imshow('blurredImage',blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()