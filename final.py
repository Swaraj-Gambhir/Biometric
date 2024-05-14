import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
from faceandhand import check
import json

# Specify the filename containing your JSON data
filename = "faceandindex.json"

# Open the file in read mode ("r")
with open(filename, "r") as json_file:

  # Use json.load() to parse the JSON data from the file
  data = json.load(json_file)
img = cv.imread('1.jpg')
model = check(img)
print(data)
hand = model.detecthandanddata()
print(hand)
face = model.detectfaceanddata()
print("Top 5 face matches")
for i in face:
  index=i[1]
  print(data[str(index)],i[0])
print("Top 5 hand matches")
for i in hand:
  index=i[1]
  print(data[str(index)],i[0])
