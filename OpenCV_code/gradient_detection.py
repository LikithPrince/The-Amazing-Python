# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
#import numpy as np


#read the image from computer
img = cv.imread('images/cat1.jpg',0)
cv.imshow("Original Image", img)

#Laplacian gradient
gradient = cv.Laplacian(img,cv.CV_64F)
cv.imshow("Laplacian Gradient", gradient)

#Sobel x gradient
gradient = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
cv.imshow("Sobel x gradient", gradient)

#Sobel y gradient
gradient = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
cv.imshow("Sobel y gradient", gradient)