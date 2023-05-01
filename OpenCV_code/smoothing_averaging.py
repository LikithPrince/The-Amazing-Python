# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
#import numpy as np

#read the image from computer
img = cv.imread('images/rough_edge_img.jpg')
cv.imshow("Original Image", img)

# perform average filtering
result = cv.blur(img,(5,5))
cv.imshow("Average Smooth Image",result)



