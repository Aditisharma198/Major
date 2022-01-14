import cv2
import numpy as np
import time
import HandTrackingModule as htm

pTIME = 0
cTIME = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img,draw=False)
    lmList = detector.findPosition(img,False)
    if len(lmList) != 0:
        print(lmList[4])
    cTIME = time.time()
    fps = 1 / (cTIME - pTIME)
    pTIME = cTIME

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
