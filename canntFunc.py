import cv2
image=cv2.imread('blurImg.png',cv2.IMREAD_GRAYSCALE)
edges=cv2.Canny(image,50,150)
cv2.imshow('original Image',image)
cv2.imshow('canny Image',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
