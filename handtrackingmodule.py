import mediapipe as mp 
import cv2 as cv
import time

class handDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,1,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHand(self,img, draw=True):
            imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
            self.results = self.hands.process(imgRGB)
            print(self.results.multi_hand_landmarks)
            if self.results.multi_hand_landmarks:
                for handLms in self.results.multi_hand_landmarks:
                    
                    if draw:
                        self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
                    # for id, lm in enumerate(handLms.landmark):
                    #     # print(id,lm)
                    #     h, w, c= img.shape
                    #     cx, cy = int(lm.x*w), int(lm.y*h)
                    #     print(id,cx,cy)

            return img
    def findPosition(self,img,handNo=0,draw=True):
        lmList =[]
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                            # print(id,lm)
                            h, w, c= img.shape
                            cx, cy = int(lm.x*w), int(lm.y*h)
                            print(id,cx,cy)
                            lmList.append([id,cx,cy])
                            if draw:
                                 cv.circle(img,(cx,cy),15,(255,0,255),cv.FILLED)
        return lmList


    # img = cv.flip(img, 1)

    







