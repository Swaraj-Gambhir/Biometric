import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap=cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = HandDetector(detectionCon=0,maxHands=2)

while True:
    success, img = cap.read()
    img = cv.flip(img,1)
    img=detector.findHands(img)
    lmList, _ = detector.findPosition(img)
    cv.imshow('Image',img)
    
    if cv.waitKey(1) & 0xFF == ord('q'): 
                    break 