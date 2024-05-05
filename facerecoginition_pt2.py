
import numpy as np
from imgbeddings import imgbeddings
from PIL import Image
import cv2 as cv
import psycopg2
import os
import pandas as pd
import numpy as np
First = True
for filename in os.listdir("stored-faces"):
    # opening the image
    img = Image.open("stored-faces/" + filename)
    # loading the `imgbeddings`
    ibed = imgbeddings()
    # calculating the embeddings
    embedding = ibed.to_embeddings(img)

    
    if First:
        First= False
        arr = embedding
        df = pd.DataFrame(arr,columns = range(768),index=[filename[:-4]])
    else:
        arr = pd.Series(np.array(embedding).reshape(768))
        df = df._append(arr,index=filename[:-4])
print(df)

