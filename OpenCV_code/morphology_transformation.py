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

#create an ones array of size 5x5
trans_kernel = np.ones((5,5), dtype="uint8")


#defining the erosion transformation
trans_image = cv.erode(img, trans_kernel, iterations=1)

#show the erosion Transformation
cv.imshow("Erode Transformation",trans_image)


#defining the dilation transformation
trans_image = cv.dilate(img, trans_kernel, iterations=1)

#show the dilation Transformation
cv.imshow("Dilate Transformation",trans_image)

#define the opening transformation
trans_image = cv.morphologyEx(img,cv.MORPH_OPEN,trans_kernel)

#show the open Transformation
cv.imshow("Open Transformation",trans_image)

#define the closing transformation
trans_image = cv.morphologyEx(img,cv.MORPH_CLOSE,trans_kernel)

#show the close Transformation
cv.imshow("Close Transformation",trans_image)


#define the gradient transformation
trans_image = cv.morphologyEx(img,cv.MORPH_GRADIENT,trans_kernel)

#show the gradient Transformation
cv.imshow("gradient Transformation",trans_image)

#define the top hat transformation
trans_image = cv.morphologyEx(img,cv.MORPH_TOPHAT,trans_kernel)

#show the top hat Transformation
cv.imshow("top hat Transformation",trans_image)


#define the black hat transformation
trans_image = cv.morphologyEx(img,cv.MORPH_BLACKHAT,trans_kernel)

#show the black hat Transformation
cv.imshow("black hat Transformation",trans_image)




