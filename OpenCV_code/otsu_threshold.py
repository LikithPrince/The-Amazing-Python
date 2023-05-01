# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
#import numpy as np

#read the image from computer
img = cv.imread('images/flower1.jpg',0)
cv.imshow("Original Image", img)

# perform Otsu threshold
thresh,thresh_img = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("Otsu threshold Image",thresh_img)

