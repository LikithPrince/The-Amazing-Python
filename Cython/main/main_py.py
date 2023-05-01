from numpy import random
import cython

def random_sum(num):
    x: cython.int
    num: cython.int
    x=sum(random.randint(num, size=(1000)))
    
    # print(x)
    return x