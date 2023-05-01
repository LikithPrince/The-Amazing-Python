# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
#import numpy as np

#read the image from computer
img = cv.imread('images/abhi2.jpg')

#show the Actual Image
cv.imshow("Original",img)

#do simple array slicing
cropped_image = img[60:200, 50:200]

cv.imshow("Cropped",cropped_image)