import cv2 as cv
import time
import handtrackingmodule as htp
pTime = 0
cTime = 0
cap= cv.VideoCapture(0)
detector = htp.handDetector()
while True:
                success,img = cap.read()
                img=detector.findHand(img)
                lmList=detector.findPosition(img)
                if len(lmList) != 0:
                    print(lmList[0])
                cTime = time.time()
                fps = 1/(cTime-pTime)
                pTime = cTime

                cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_DUPLEX,3,(240,100,234),2)
                cv.imshow("Image",img)

                if cv.waitKey(1) & 0xFF == ord('q'): 
                    break
