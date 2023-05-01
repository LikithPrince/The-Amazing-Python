

# from main import *
# from main_py import *
import timeit

py=timeit.timeit('main_py.random_sum(500000)', setup='import main_py',number=10000)
cy=timeit.timeit('main.random_sum(500000)', setup='import main',number=10000)

print("Cython is taking :",round(cy,2),"sec")
print("Python is taking :",round(py,2),"sec")

print(f'Cython is {round((py/cy),2)} times faster than Python!')