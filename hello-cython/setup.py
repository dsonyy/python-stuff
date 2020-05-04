from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Hello App',
    ext_modules=cythonize("hello.py"),
    zip_safe=False,
)