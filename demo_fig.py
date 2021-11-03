# python program to demonstrate python matplotlib figure
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,4))
#ax1 = fig.add_subplot(121)
#ax2 = fig.add_subplot(122)
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# or
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

ax1.plot([1, 2, 3], [3, 4, 5], 'bs:')
#ax2.barh([0.5, 1, 2.5], [0, 1, 2])

plt.show()

import numpy as np

plt.style.use('seaborn')
x = [ i for i in range(1, 11)]
#y = [8, 7, 6, 4, 5, 6, 7, 8, 9, 10]
y = x

plt.xticks(np.arange(11))
plt.yticks(np.arange(11))

points_size = [ i*10 for i in range(1, 11)]
print(points_size)

plt.scatter(x, y, s=points_size, c='g')
plt.title("Scatter Plot", fontsize=25)

plt.xlabel('x-axis', fontsize=18)
plt.ylabel('y-axis', fontsize=18)

plt.show()

