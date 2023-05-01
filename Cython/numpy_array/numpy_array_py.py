import numpy as np
import pdb

def np_array():
    
    arr1=np.load(r"/mnt/c/Users/LikithP/OneDrive - Ennoventure Inc/Documents/Likith_python/Practice/Cython/puppy.npy")
    return(arr1)


print(np_array())