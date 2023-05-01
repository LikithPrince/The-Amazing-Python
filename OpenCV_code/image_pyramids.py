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

#up sample pyramid
up1 = cv.pyrUp(img)
cv.imshow("up1 Image", up1)
up2 = cv.pyrUp(up1)
cv.imshow("up2 Image", up2)

#down sample pyramid
down1 = cv.pyrDown(img)
cv.imshow("down1 Image", down1)
down2 = cv.pyrDown(down1)
cv.imshow("down2 Image", down2)



