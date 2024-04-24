import cv2

alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + alg)

cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    if img is not None and img.size != 0:  # Check if img is not None and not empty
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        print("Error: Image is empty!")
        break

    face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("FaceDetection", img)
    key = cv2.waitKey(10)
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()


import cv2

alg="haarcascade_frontalface_default.xml"
haar_cascade=cv2.CascadeClassifier(alg)
cam=cv2.VideoCapture(0)

while True:
    _,img=cam.read()
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(grayImg,1.3,4)
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("FaceDetection",img)
    key=cv2.waitKey(10)
    if key == ord("q"):
       break
cam.release()
cv2.destroyAllWindows()
