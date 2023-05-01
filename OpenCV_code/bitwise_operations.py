# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
#import numpy as np

#read the image from computer
img1 = cv.imread('images/left_circle.jpg')
img2 = cv.imread('images/right_circle.jpg')


cv.imshow("Image 1",img1)
cv.imshow("Image 2",img2)

#perfom the bitwise operations
result = cv.bitwise_and(img1, img2)
cv.imshow("AND",result)

result = cv.bitwise_or(img1, img2)
cv.imshow("OR",result)

result = cv.bitwise_xor(img1, img2)
cv.imshow("XOR",result)

result = cv.bitwise_not(img1)
cv.imshow("NOT",result)




