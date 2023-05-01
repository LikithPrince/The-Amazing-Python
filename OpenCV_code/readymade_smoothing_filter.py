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

# perform gaussian Blur filtering
result = cv.GaussianBlur(img,(5,5),0)
cv.imshow("gaussian Smooth Image",result)

#read the image from computer
img = cv.imread('images/noisy_img.jpg')
cv.imshow("Original Image", img)

# perform median Blur filtering
result = cv.medianBlur(img,5)
cv.imshow("median Blur Smooth Image",result)

#read the image from computer
img = cv.imread('images/pixelated_img.jpg')
cv.imshow("Original Image", img)

# perform bilateral filtering
result = cv.bilateralFilter(img,10,75,75)
cv.imshow("bilateral Smooth Image",result)


