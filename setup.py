from setuptools import setup, find_packages

setup(
    name="fuNEGF",
    version="0.1",
    packages=find_packages(),
    author="L. Vojacek",
    author_email="libor.vojacek@cea.fr",
    install_requires=[
        "numpy",    
        "matplotlib",
        "scipy",
        "pytest",
        "pytest-cov",
        "pytest-mpl",
    ],
)
