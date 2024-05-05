import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import pandas as pd
import numpy as np
from numpy.linalg import norm
cap= cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
def text(img,text='none'):
        org = (100, 100)
        font = cv.FONT_HERSHEY_COMPLEX
        fontScale = 0.5
        color = (0,0,0)  #(B, G, R)
        thickness = 1
        lineType = cv.LINE_AA
        bottomLeftOrigin = False
        
        # Syntax>> cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
        
        img_text = cv.putText(img, text, org, font, fontScale, color, thickness, lineType, bottomLeftOrigin)
        return img_text
 
df =pd.read_csv('table.csv',index_col=False)
detector = HandDetector(detectionCon=0,maxHands=2)

while True:
    success, img =cap.read()
    img = cv.flip(img,1)
    img=detector.findHands(img)
    
    lmList, _ = detector.findPosition(img)
    q=img.copy()
    x=1
    li=[]
    o=""
    if lmList:
 
        for i in range(0,21):
                  for j in range(i+1,21):
                              x,_,_=detector.findDistance(i,j,img)
                              li.append(x)
        j=1
        for index in df.index:
                row = np.array(df.loc[index] ) # Access row by index using .loc
                cosine = np.dot(row,li)/(norm(row)*norm(li))
                cosine =round(cosine, 3)
                o=o+" Cosine Similarity"+ str(j)+":"+str(cosine)
                j+=1
        
        
    
    
    print(li)
    q = text(q,o)

    cv.imshow("Image",q)

    if cv.waitKey(1) & 0xFF == ord('q'): 
                    break
    
     