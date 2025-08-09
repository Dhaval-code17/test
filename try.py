import cv2 as cv

img = cv.imread('photos/lufy.jpg')

cv.imshow('lufy', img)

cv.waitKey(0)