import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
cap= cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
color=(255,100,0)
detector = HandDetector(detectionCon=0)
cx,cy,w,h=100,100,200,200


class DragRect:
        def __init__(self,posCenter, size =[200,200]):
                self.posCenter = posCenter
                self.size = size
        def update(self,cursor):
                cx,cy=self.posCenter
                w,h=self.size
                print(cursor)
                if cx-w//2<cursor[0]<cx+w//2 and cy-h//2<cursor[1]<cy+h//2:
                        cx=cursor[0]
                        cy=cursor[1]
                        self.posCenter = cx,cy



rect = DragRect([150,150])
while True:
    success, img =cap.read()
    img = cv.flip(img,1)
    img=detector.findHands(img)
    lmList, _ = detector.findPosition(img)
    if lmList:    
        l,_,_=detector.findDistance(8,12,img)
        
        if l<30:
                cursor = lmList[8]
                # Call update here
                rect.update(cursor)
    cx,cy=rect.posCenter
    w,h=rect.size
    cv.rectangle(img,(cx-w//2,cy-h//2),(cx+w//2,cy+h//2),color,cv.FILLED)
    
    cv.imshow("Image",img)
    if cv.waitKey(1) & 0xFF == ord('q'): 
                    break
