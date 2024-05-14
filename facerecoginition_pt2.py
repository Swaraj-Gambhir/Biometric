
import numpy as np
from imgbeddings import imgbeddings
from PIL import Image
import cv2 as cv
import psycopg2
import os
import pandas as pd
import numpy as np
import json
First = True
dic={}
no=0
for filename in os.listdir("stored-faces"):
    # opening the image
    img = Image.open("stored-faces/" + filename)
    # loading the `imgbeddings`
    ibed = imgbeddings()
    # calculating the embeddings
    embedding = ibed.to_embeddings(img)

    
    if First:
        First= False
        arr = embedding.reshape(768)
        # single_row_df = pd.Series(arr, name=filename[:-4])
        df = pd.DataFrame([arr], columns=range(768), index=[filename[:-4]])
        dic[no]=filename[:-4]
        no+=1


# Convert the Series to a DataFrame (single row)
        
    else:
        arr = pd.Series(np.array(embedding).reshape(768), name=filename[:-4])
        
        df = df._append(arr, ignore_index=True)
        dic[no]=filename[:-4]
        no+=1
        

        
df.to_csv('facedata.csv',index=False)
# Open a file for writing in text mode (use 'w' for write)
with open("faceandindex.json", "w") as json_file:

  # Use json.dump() to write the dictionary directly to the file
  json.dump(dic, json_file, indent=4) 