from numpy import random


cpdef random_sum(int num):
    cdef int x
    
    x=sum(random.randint(num, size=(100)))

    return x