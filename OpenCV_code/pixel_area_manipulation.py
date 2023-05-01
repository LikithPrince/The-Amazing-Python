# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv

#read the image from computer
img = cv.imread('images/abhi1.jpg')

#show the image
cv.imshow("abhi photo original",img)

#get pixel at row,column position
pixel = img[120,120]
print("Color intensity at (120,120) pixel is Blue: {}, Green: {}, Red:{}".format(pixel[0], pixel[1], pixel[2]))

#get only single color value for a pixel
red_pixel = img[120,120,2]
print("Color intensity of red pixel at (120,120) is {}".format(red_pixel))

#set the color of pixel at 120x120 to green
img[120,120] = (0,255,0)
pixel = img[120,120]
print("Color intensity at (120,120) pixel is Blue: {}, Green: {}, Red:{}".format(pixel[0], pixel[1], pixel[2]))

#get the region from the image
slice = img[0:120, 0:120]
cv.imshow("sliced image",slice)

#set the color of area at 0:120 till 0:120 to green
img[0:120,0:120] = (0,255,0)
cv.imshow("manipulated slice of image",img)

#printing properties of image
print("shape of image")
print(img.shape)
print("total no of pixels in the image")
print(img.size)
print("data type of image")
print(img.dtype)
