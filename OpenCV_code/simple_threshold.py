# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
#import numpy as np

#read the image from computer
img = cv.imread('images/brain_ct.jpg')
cv.imshow("Original Image", img)

# perform simple threshold
thresh,thresh_img = cv.threshold(img,130,255,cv.THRESH_BINARY)
cv.imshow("simple threshold Image",thresh_img)

