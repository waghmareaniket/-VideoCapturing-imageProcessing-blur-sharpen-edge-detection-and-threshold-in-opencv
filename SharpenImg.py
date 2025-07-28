import cv2
import numpy as np
image=cv2.imread('blurImg.png')
sharp_kernel=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
sharpp=cv2.filter2D(image,-1,sharp_kernel)
cv2.imshow('oringinal image',image)
cv2.imshow('sharpImg',sharpp)
cv2.waitKey(0)
cv2.destroyAllWindows()