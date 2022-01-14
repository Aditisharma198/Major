import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

pTIME=0
cTIME=0


while True:
    success, img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(img)
    #print(results.multi_hand_landmarks)


    if results.multi_hand_landmarks:
        for handL in results.multi_hand_landmarks:
            for id, ln in enumerate(handL.landmark):
                #print(id,ln)
                h, w, c = img.shape
                cx, cy=int(ln.x*w),int(ln.y*h)
                print(id, cx , cy)
                if id==16:
                    cv2.circle(img, (cx,cy),15,(255,0,255),cv2.FILLED)

            mpDraw.draw_landmarks(img,handL,mpHands.HAND_CONNECTIONS)

    cTIME = time.time()
    fps = 1 / (cTIME-pTIME)
    pTIME = cTIME

    cv2.putText(img, str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)



    cv2.imshow("Image",img)
    cv2.waitKey(1)