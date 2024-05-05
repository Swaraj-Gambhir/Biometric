import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
def text(img,text='none'):
        org = (100, 100)
        font = cv.FONT_HERSHEY_COMPLEX
        fontScale = 1
        color = (0,0,255)  #(B, G, R)
        thickness = 2
        lineType = cv.LINE_AA
        bottomLeftOrigin = False
        
        # Syntax>> cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
        
        img_text = cv.putText(img, text, org, font, fontScale, color, thickness, lineType, bottomLeftOrigin)
        return img_text
img = cv.imread('img1.jpg')
detector = HandDetector(detectionCon=0,maxHands=2)
img=detector.findHands(img)
lmList, _ = detector.findPosition(img)
if lmList:
        l,_,_=detector.findDistance(8,12,img)
if l:
            l=int(l)
img = text(img,str(l))
cv.imwrite('img1_dist.jpg', img)