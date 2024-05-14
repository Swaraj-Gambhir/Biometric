import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import pandas as pd
import numpy as np
from numpy.linalg import norm
import numpy as np
from imgbeddings import imgbeddings
from PIL import Image
import psycopg2
import os

def func(a):
        return a[0]
class check():
        def __init__(self,img):
                self.imag=img
        def detecthandanddata(self):
                df =pd.read_csv('handdata.csv',index_col=False)
                detector = HandDetector(detectionCon=0,maxHands=2)
                img = cv.flip(self.imag,1)
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
                cos=[]
                # print(li)
                for index in df.index:
                        row = np.array(df.loc[index] ) # Access row by index using .loc
                        cosine = np.dot(row,li)/(norm(row)*norm(li))
                        cosine =round(cosine, 3)
                    
                        cos.append([cosine,index])
                cos.sort(key=func,reverse=True)
                print(cos)
                top5=cos[:5]
                return top5
        def detectfaceanddata(self):
                alg = "haarcascade_frontalface_default.xml"
# passing the algorithm to OpenCV
                haar_cascade = cv.CascadeClassifier(alg) 
                df =pd.read_csv('facedata.csv', index_col=False)
                # detector = HandDetector(detectionCon=0,maxHands=2)
                img = cv.flip(self.imag,1)

                # creating a black and white version of the image
                gray_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
                # detecting the faces
                faces = haar_cascade.detectMultiScale(
                    gray_img, scaleFactor=1.05, minNeighbors=1, minSize=(100, 100)
                )
               
                i = 0
                filename  = 'test.png'
                # for each face detected
                for x, y, w, h in faces:
                    # crop the image to select only the face
                    cropped_image = img[y : y + h, x : x + w]
                target_file_name = 'stored-faces/' + filename 
                cv.imwrite(
                target_file_name,
                cropped_image,
                );
                cropped_image=Image.open("stored-faces/" + filename)

                ibed = imgbeddings()
    # calculating the embeddings
                embedding = ibed.to_embeddings(cropped_image)
                arr = embedding.reshape(768)
                

                
               
                cos=[]
                for index in df.index:
                        row = np.array(df.loc[index] ) # Access row by index using .loc
                        print(row.shape)
                        cosine = np.dot(row,arr)/(norm(row)*norm(arr))
                        cosine =round(cosine, 3)
                    
                        cos.append([cosine,index])
                cos.sort(key=func,reverse=True)
                top5=cos[:5]
                return top5


                

