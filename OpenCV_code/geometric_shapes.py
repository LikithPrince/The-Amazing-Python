# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv
import numpy as np


#create a black image (canvas) of black color
#using numpy zeros method for a zeros array
zeros_array = np.zeros((500,500,3), dtype="uint8")

#draw the line
img = cv.line(zeros_array, (0,0),(500,500),(255,255,255),2)

#draw the circle
img = cv.circle(img, (250,250),100,(0,255,0),2)

#draw the rectangle
img = cv.rectangle(img, (50,50),(470,470),(0,0,255),4)

#draw the ellipse
img = cv.ellipse(img, (200,200),(100,50),0,0,360,(255,0,0),2)

#draw the polygon
#1. Create a numpy array of vertices
#2. Change the shape of numpy array to -1,1,2
#3. Draw the polygon using these vertices
vertices = np.array([[170,400],[150,100],[250,200],[250,300]], np.int32)
vertices = vertices.reshape((-1,1,2))
img = cv.polylines(img,[vertices],True,(0,255,255),5)

#write the text
img = cv.putText(img, 'Hello OpenCV', (50,50),cv.FONT_HERSHEY_SIMPLEX,2,(0,0,255))

#show the Geometric Shapes
cv.imshow("Geometric Shapes",img)





