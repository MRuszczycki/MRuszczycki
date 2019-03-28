from distutils.core import setup
from Cython.Build import cythonize


setup(
    ext_modules = cythonize("J_Do_It_2.py")
)