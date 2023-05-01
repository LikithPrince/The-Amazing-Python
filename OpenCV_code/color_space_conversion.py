# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
#import numpy as np

#read the image from computer
img = cv.imread('images/dog1.jpg')

#show the BGR image
cv.imshow("BGR Color Space",img)

#show the gray color space image
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Color Space",gray)

#show the HSV color space image
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV Color Space",hsv)

#show the LAB color space image
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB Color Space",lab)




