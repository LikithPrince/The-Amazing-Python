# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
import numpy as np

#read the image from computer
img = cv.imread('images/shirt1.jpg')

#show the image
cv.imshow("shirt1 photo original",img)

#split the color channels
blue,green,red = cv.split(img)

#show the blue channel intensity
cv.imshow("blue channel intensity",blue)
#show the green channel intensity
cv.imshow("green channel intensity",green)
#show the red channel intensity
cv.imshow("red channel intensity",red)

#merging the channels
img_merged = cv.merge((blue,green,red))

#show the merged image
cv.imshow("shirt1 photo merged",img_merged)

#creating a zero array same size as that of our image
zeros_array = np.zeros(img_merged.shape[:2], dtype="uint8")

red_only_image = cv.merge((zeros_array,zeros_array,red))
#show the red only channel image
cv.imshow("shirt1 red only channel image",red_only_image)

green_only_image = cv.merge((zeros_array,green,zeros_array))
#show the green only channel image
cv.imshow("shirt1 green only channel image",green_only_image)

blue_only_image = cv.merge((blue,zeros_array,zeros_array))
#show the blue only channel image
cv.imshow("shirt1 blue only channel image",blue_only_image)





