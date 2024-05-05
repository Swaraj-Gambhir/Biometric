import cv2 as cv
import os
# loading the haar case algorithm file into alg variable
alg = "haarcascade_frontalface_default.xml"
# passing the algorithm to OpenCV
haar_cascade = cv.CascadeClassifier(alg) 
for filename in os.listdir("face_images"):

    # reading the image
    img = cv.imread("face_images/"+filename, 0)
    # creating a black and white version of the image
    gray_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    # detecting the faces
    faces = haar_cascade.detectMultiScale(
        gray_img, scaleFactor=1.05, minNeighbors=1, minSize=(100, 100)
    )
    print(faces)
    i = 0
    # for each face detected
    for x, y, w, h in faces:
        # crop the image to select only the face
        cropped_image = img[y : y + h, x : x + w]
        # loading the target image path into target_file_name variable  - replace <INSERT YOUR TARGET IMAGE NAME HERE> with the path to your target image
        target_file_name = 'stored-faces/' + filename 
        cv.imwrite(
            target_file_name,
            cropped_image,
        );



# Part 2 of the code


# Cosine Similarity
# # import required libraries
# import numpy as np
# from numpy.linalg import norm
 
# # define two lists or array
# A = np.array([2,1,2,3,2,9])
# B = np.array([3,4,2,4,5,5])
 
# print("A:", A)
# print("B:", B)
 
# # compute cosine similarity
# cosine = np.dot(A,B)/(norm(A)*norm(B))
# print("Cosine Similarity:", cosine)


