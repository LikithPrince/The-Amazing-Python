import numpy as np

# We now need to fix a datatype for our arrays. I've used the variable
# DTYPE for this, which is assigned to the usual NumPy runtime
# type info object.
DTYPE = np.intc



cpdef np_array():
    cdef Py_ssize_t arr1
    arr1=np.load(r"/mnt/c/Users/LikithP/OneDrive - Ennoventure Inc/Documents/Likith_python/Practice/Cython/puppy.npy")
    return(arr1)


print(np_array())

