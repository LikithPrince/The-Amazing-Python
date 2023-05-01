# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
import numpy as np

#read the image from computer
img = cv.imread('images/dog1.jpg')

#show the Actual Image
cv.imshow("Original",img)

resized = cv.resize(img,None,fx=2,fy=2,interpolation = cv.INTER_CUBIC)
#show the Scaled up Image
cv.imshow("Scaled up",resized)

resized = cv.resize(img,None,fx=0.5,fy=0.5,interpolation = cv.INTER_AREA)
#show the Scaled up Image
cv.imshow("Scaled down",resized)
