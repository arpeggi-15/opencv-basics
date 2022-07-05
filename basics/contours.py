import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

#Finding contours using Canny edges
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# canny = cv.Canny(blur, 125,175)
# cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(grpypythoay, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)