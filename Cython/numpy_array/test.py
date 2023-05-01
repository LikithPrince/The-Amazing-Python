
import timeit

py=timeit.timeit('numpy_array_py.np_array()', setup='import numpy_array_py',number=1000)
cy=timeit.timeit('numpy_array_cy.np_array()', setup='import numpy_array_cy',number=1000)

print("Cython is taking :",round(cy,2),"sec")
print("Python is taking :",round(py,2),"sec")

print(f'Cython is {round((py/cy),2)} times faster than Python!')