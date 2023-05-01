import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('Sales_Demo_Front.png',0)
resized=cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)
# imgplot=plt.imshow(resized)
cv.imshow("resized",resized)