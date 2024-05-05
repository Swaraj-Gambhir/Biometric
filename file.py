import pandas as pd
import numpy as np
from numpy.linalg import norm
import os
# df =pd.read_csv('table.csv',index_col=False)
# print(df)
# x=[62.0966987850401, 123.4382436686459, 170.66048165876012, 208.568933448872, 158.64740779476983, 218.8332698654389, 255.03137061938085, 288.00868042473996, 159.10059710761615, 224.72205054244233, 263.7366110345699, 297.4104907362886, 151.40013210033868, 211.19185590358356, 247.2023462671825, 279.3027031734566, 138.27870407260838, 186.29009635512028, 217.7200036744442, 247.40654801358835]

# for index in df.index:
#     row = np.array(df.loc[index] ) # Access row by index using .loc
#     cosine = np.dot(row,x)/(norm(row)*norm(x))
#     print("Cosine Similarity:", cosine)


# for filename in os.listdir("stored-faces"):
#     print(filename[:-4])