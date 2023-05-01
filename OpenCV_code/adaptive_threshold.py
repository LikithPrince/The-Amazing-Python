
#import opencv library
import cv2 as cv
#import numpy as np

#read the image from computer
img = cv.imread('images/flower1.jpg',0)
cv.imshow("Original Image", img)

# perform adaptive threshold
thresh_img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
cv.imshow("Adaptive Mean C threshold Image",thresh_img)

thresh_img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
cv.imshow("Adaptive Gaussian C threshold Image",thresh_img)
