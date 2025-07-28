import cv2
img=cv2.imread('blurImg.png',cv2.IMREAD_GRAYSCALE)
ret,thresh=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
cv2.imshow('original Image',img)
cv2.imshow('thresh Image',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
