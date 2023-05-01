
from PIL import Image
import cv2
img1=Image.open('IMG_5409-crop.jpg')
# img2=Image.open('puppy1.jpg')
print(img1.size)
# print(img2.size)
img3=img1.crop((0,300,0,300))
# print(img3.size)
img4=cv2.imwrite("img.jpg",img3)
# cv2.imwrite("img.jpg",img4)