import cv2
import time

cam = cv2.VideoCapture(2)
time.sleep(1)
while True:
    _,img = cam.read()
    cv2.imshow("cameraFeed",img)
    Key = cv2.waitKey(1) & 0xFF
    if Key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()


