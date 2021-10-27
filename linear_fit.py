import numpy as np
import matplotlib.pyplot as plt

# x co-ordinates
x = np.arange(0, 9)
A = np.array([x, np.ones(9)])
print("x:\n", x)
print("A:\n", A)

# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]

# obtaining the coefficients of the regression line
w = np.linalg.lstsq(A.T, y)[0]

# plotting the line
line = w[0]*x + w[1]
plt.plot(x, line, 'r-')
plt.plot(x, y, 'o')
plt.show()
