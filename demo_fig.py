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