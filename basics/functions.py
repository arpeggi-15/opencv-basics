import cv2 as cv
from cv2 import imread

img = imread('Photos/park.jpg')

cv.imshow('Park', img)

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)


#Blurring an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

#eroding the image
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#Resize an Image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", resized)

#Cropping an Image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)