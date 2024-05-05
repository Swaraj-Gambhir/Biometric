import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
cap= cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = HandDetector(detectionCon=0,maxHands=2)
cx,cy,w,h=100,100,200,200
lis=[]
class ColorPencil:
        def __init__(self,posCenter, size =[20,20]):
                self.posCenter = posCenter
                self.size = size
                self.lis = []
                self.color=(0,0,255)
                self.delete  = False
        def update(self,cursor):
                # if cx-w//2<cursor[0]<cx+w//2 and cy-h//2<cursor[1]<cy+h//2:
                cx=cursor[0]
                cy=cursor[1]
                dic={}
                self.posCenter = cx,cy
                if [cx,cy] not in self.lis:
                    dic['point']=[cx,cy]
                    dic['color']=self.color
                    self.lis.append(dic)
        def colorpallete(self,cursor):
                cx,cy=cursor
                if 0<cx<100 and 0<cy<100:
                    self.color=(255,0,0)
                    self.delete=False
                if 200<cx<300 and 0<cy<100:
                    self.color=(0,255,0)
                    self.delete=False
                if 400<cx<500 and 0<cy<100:
                    self.color=(0,0,255)
                    self.delete=False
                if 700<cx<800 and 0<cy<100:
                        self.delete=True
        def removelement(self,cursor):
                lisw = [i['point'] for i in self.lis]
                if cursor in lisw:
                       print("Delete Mode")
                       index=lisw.index(cursor)
                       self.lis.pop(index)
                


pencil = ColorPencil((0,0))
while True:
    success, img =cap.read()
    img = cv.flip(img,1)
    img=detector.findHands(img,draw=False)
    lmList, _ = detector.findPosition(img,draw=False)
    if lmList:    
        # l,_,_=detector.findDistance(8,12,img)
        # print(l)

                cursor = lmList[8]
                # Call update here
                # print(cursor)
                if pencil.delete == False:
                    pencil.update(cursor)
                pencil.colorpallete(cursor)
                
                       
                        
    w,h=10,10

    # print(rect.lis)
    if pencil.delete == True:
                
                
                
                pencil.removelement(cursor)
    
    for i in pencil.lis:
            
            cx,cy=i['point']
            cv.rectangle(img,(cx-w//2,cy-h//2),(cx+w//2,cy+h//2),i['color'],cv.FILLED)
    cv.rectangle(img,(0,0),(100,100),(255,0,0),cv.FILLED)
    cv.rectangle(img,(200,0),(300,100),(0,255,0),cv.FILLED)
    cv.rectangle(img,(400,0),(500,100),(0,0,255),cv.FILLED)
    cv.rectangle(img,(700,0),(800,100),(255,255,255),cv.FILLED)
    print(len(pencil.lis))
    cv.imshow("Image",img)
    if cv.waitKey(1) & 0xFF == ord('q'): 
                    break
