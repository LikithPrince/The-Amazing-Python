
# from distutils.core import setup
# from Cython.Build import cythonize
# setup(ext_modules = cythonize('compiled/main.pyx'))

from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("main.pyx"))