# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
from matplotlib import pyplot as plt
#import numpy as np


#read the image from computer
img = cv.imread('images/shirt1.jpg',0)
cv.imshow("Original Image", img)

plt.hist(img.ravel(),256,[0,256])
plt.show