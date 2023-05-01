
from PIL import Image
from numpy import asarray
import numpy as np


# load the image
image = Image.open('puppy.jpg')
# convert image to numpy array
data = asarray(image)
print(type(data))
# summarize shape
print(data.shape)
np.save("puppy.npy",data)