# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
#import numpy as np

#read the image from computer
img1 = cv.imread('images/abhi2.jpg')
img2 = cv.imread('images/flower1.jpg')

#do simple array slicing
cropped_image1 = img1[60:200, 50:200]
cropped_image2 = img2[60:200, 50:200]

cv.imshow("Image 1",cropped_image1)
cv.imshow("Image 2",cropped_image2)

#adding the images
added_image = cv.add(cropped_image1, cropped_image2)
cv.imshow("Added",added_image)

#subtracting the images
subtracted_image = cv.subtract(cropped_image1, cropped_image2)
cv.imshow("Subtracted",subtracted_image)



