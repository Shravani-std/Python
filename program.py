import cv2
img = cv2.imread("sample1.jpg")
cv2.imshow("Pantech Logo",img)
cv2.imwrite("PantechLogo.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
