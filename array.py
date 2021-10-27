# Python program to demonstrate
# basic numpy array characteristics
import numpy as np

# create array object
arr = np.array( [[ 1, 2, 3], [ 4, 2, 5]])

# print type of arr object
print("Array is of type: ", type(arr))

# print array dimension (axes)
print("No. of dimensions: ", arr.ndim)

# print shape of array
print("Shape of array: ", arr.shape)

# print size of array(total number of elements)
print("Size of array: ", arr.size)

# print type of elements in array
print("Array stores elements of type: ", arr.dtype)
