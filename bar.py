# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt

print(plt)
# create new figure
fig = plt.figure()
# create axes
# one row, one col, plot number
ax = fig.add_subplot(111)
print(ax)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
ax.set_xlim(0.5, 4.5)

plt.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
