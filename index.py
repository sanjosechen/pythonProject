# python program to demonstrate indexing in numpy
import numpy as np

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# slice array
temp = arr[:2, ::2]
print("Array with first 2 rows and alternate columns(0 and 2):\n", temp)

# integer array indexing
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print("Elements at indices (0, 3), (1, 2), 2, 1), (3, 0):\n", temp)

# boolean array indexing
cond = arr > 0 # is a boolean array
print("cond:\n", cond)
temp = arr[cond]
print("Elements greater than 0:\n", temp)

