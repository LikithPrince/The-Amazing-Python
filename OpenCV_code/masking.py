# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
#import numpy as np

#read the image from computer
img = cv.imread('images/monkey1.jpg')
mask = cv.imread('images/left_circle.jpg')

result = cv.bitwise_and(img, mask)
cv.imshow("Masked Image", result)



