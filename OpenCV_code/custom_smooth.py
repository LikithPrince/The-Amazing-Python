# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
import numpy as np

#read the image from computer
img = cv.imread('images/pixelated_img.jpg')
cv.imshow("Original Image", img)

#create kernel for convolution
custom_kernel = np.ones((5,5),np.float32)/25
# perform convlution
result = cv.filter2D(img, -1, custom_kernel)
cv.imshow("Custom Smooth Image", result)



