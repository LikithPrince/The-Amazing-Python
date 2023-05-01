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

#define the transformation matrix
trans_matrix = cv.getRotationMatrix2D((img.shape[1]//2,img.shape[0]//2),75,1)
#rotated the image
rotated_image = cv.warpAffine(img,trans_matrix,(img.shape[1],img.shape[0]))
#show the rotated Image
cv.imshow("Rotated",rotated_image)