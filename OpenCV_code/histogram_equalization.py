# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
#import numpy as np


#read the image from computer
img = cv.imread('images/beach.jpg',0)
cv.imshow("Original Image", img)

#perform equalization
corrected_img = cv.equalizeHist(img)
cv.imshow("Equalized Image", corrected_img)
