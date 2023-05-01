# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
#import numpy as np

#read the image from computer
img = cv.imread('images/dog1.jpg')

#show the Actual Image
cv.imshow("Original",img)


#flipped images
flipped_image = cv.flip(img,1)
#show the Flipped Image
cv.imshow("Flipped Horizontal",flipped_image)

flipped_image = cv.flip(img,0)
#show the Flipped Image
cv.imshow("Flipped Veritical",flipped_image)

flipped_image = cv.flip(img,-1)
#show the Flipped Image
cv.imshow("Flipped Both Directions",flipped_image)