import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import pandas as pd
import os 
l=None
dick={}
a ="0-"
first = True
for filen in os.listdir("face_images"):
      img = cv.imread("face_images/" + filen)
      # print(img)
      dick={}
      for i in range(0,21):
            for j in range(i+1,21):
                  
                        text = str(j) + '-'+ str(i)
                        dick[text] = 0
      detector = HandDetector(detectionCon=0,maxHands=1)
      img=detector.findHands(img)
      lmList, _ = detector.findPosition(img)
      if lmList:
            for i in range(0,21):
                  for j in range(i+1,21):
                              dick[str(j) + '-'+ str(i)],_,_=detector.findDistance(i,j,img)

      print(filen)
      if first:
            first = False
            df=pd.DataFrame(dick, index=[0])
      else:
            df=df._append(dick, ignore_index=True)
      cv.imwrite(f'hand_images_dist/dist_{filen}', img)

df.to_csv('handdata.csv',index=False)