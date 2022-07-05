import cv2 as cv
from cv2 import rectangle
from cv2 import bitwise_and
from cv2 import bitwise_or
from cv2 import bitwise_not
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

circle = cv.circle(blank.copy(),(200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


##Bitwise AND ---> intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND', bitwise_and)

##Bitwise OR ----> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR', bitwise_or)

##Bitwise XOR---->  non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR', bitwise_xor)

##Bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Rectangle Not',bitwise_not)

##Bitwise XOR - Bitwise OR = Bitwise AND
##Bitwise AND - Bitwise OR = Bitwise XOR



cv.waitKey(0)