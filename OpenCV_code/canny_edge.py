# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
#import numpy as np


#read the image from computer
img = cv.imread('images/cat1.jpg')
cv.imshow("Original Image", img)

#canny edge detection code
edges = cv.Canny(img, 110, 210)
cv.imshow("Edge Detected Image", edges)


