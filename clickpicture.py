import cv2 as cv
cap= cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

success, img =cap.read()
img = cv.flip(img,1)
cv.imwrite('img1.jpg', img)

