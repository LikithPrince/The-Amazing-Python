# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv

#read the image from computer
img = cv.imread('images/abhi1.jpg',0)
#print the shape of image
print(img.shape)
#write the image to computer
cv.imwrite('images/abhi1gray.jpg',img)
#show the image
cv.imshow("abhi photo",img)
