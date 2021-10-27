# python program to demonstrate basic operations on single array
import numpy as np

a = np.array([1, 2, 5, 3])

# add 1 to every element
print("Adding 1 to every element:\n", a + 1)

# subtract 3 from each element
print("Subtracting 3 from each element:\n", a - 3)

# multiply each element by 10
print("Multiplying each element by 10:\n", a * 10)

# squre each element
print("Squaring each element:\n", a**2)

# modify existing array
a *= 2
print("Doubleed each element:\n", a)

# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])
print("Original array:\n", a)
print("Transpose of array:\n", a.T)

# maximum element of array
print("Largest element is:\n", a.max())
print("Row-wise maximum elements:\n", a.max(axis = 1))

# minimum element of array
print("Column-wise mininum elements:\n", a.min(axis = 0))

# sum of array elements
print("Sum of all array elements:\n", a.sum())

# cumulative sum along each row
print("Cumulative sum along each row:\n", a.cumsum(axis = 1))

# python program to demonstrate binary operators
a = np.array([[1, 2], [3, 4]])
b = np.array([[4, 3], [2, 1]])

# add arrays
print("Array sum:\n", a + b)

# multiply arrays(elementwise multiplication)
print("Array multiplication:\n", a * b)

# matrix multiplication
print("Matrix multiplication:\n", a.dot(b))

# create array of sine values
a = np.array([0, np.pi/2, np.pi])
print("Sine values of array elements:\n", np.sin(a))

# expoential values
a = np.array([0, 1, 2, 3])
print("Exponent of array elements:\n", np.exp(a))

# square root of array values
print("Square root of array elements:\n", np.sqrt(a))




