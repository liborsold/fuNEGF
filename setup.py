# make a setup file for the package

from setuptools import setup, find_packages

setup(
    name='fuNEGF',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'pytest',
        'pytest-cov',
        'pytest-mpl'
    ]
)