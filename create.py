# python program to demonstrate
# array creation
import numpy as np

# create array from list with type float
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print("Array created using passed list: \n", a)

# create array from typle
b = np.array((1, 3, 2))
print("Array created using passed typle:\n", b)

# create 3x4 array with all zeros
c = np.zeros((3, 4))
print("Array initialized to all zeros:\n", c)

# create a constant value array of complex type
d = np.full((3, 3), 6, dtype = 'complex')
print("Array initialized with all 6s. Array type is complex:\n", d)

# create an array with random values
e = np.random.random((2, 2))
print("A random array: \n", e)

# create a sequence of integers from 0 to 30 with
# steps of 5
f = np.arange(0, 30, 5)
print("Array with steps of 5:\n", f)

# create 10 values between 0 and 5
g = np.linspace(0, 5, 10)
print("Array with 10 values between 0 and 5:\n", g)

# reshape 3x4 array to 2x2x3 array
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])
newarr = arr.reshape(2, 2, 3)

print("Original array:\n", arr)
print("Reshaped array:\n", newarr)

# flatten array
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()
print("Original array:\n", arr)
print("flattened array:\n", flarr)



