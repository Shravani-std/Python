import cv2

import imutils
img = cv2.imread("sample.jpg")
resizing = imutils.resize(img,width-20)
cv3.imwrite("resizedimage.jpg",resizeimg)
