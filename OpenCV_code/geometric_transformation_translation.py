# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
import numpy as np

#read the image from computer
img = cv.imread('images/dog1.jpg')

#show the Actual Image
cv.imshow("Original",img)

#define the transformation matrix
trans_matrix = np.float32([[1,0,-50],[0,1,-25]])
#shifting the image
shifted_image = cv.warpAffine(img,trans_matrix,(img.shape[1],img.shape[0]))
#show the Shifted Image
cv.imshow("Shifted",shifted_image)