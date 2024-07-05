import numpy

try:
    import numpy as np
    print("NumPy is installed.")
    print("NumPy version:", np.__version__)
except ModuleNotFoundError:
    print("NumPy is not installed.")
    print("To install NumPy, use the following command:")
    print("pip install numpy")
