# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from matplotlib import pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def plot_line():
    x = [5, 2, 9, 4, 7]
    y = [10, 5, 8, 4, 2]

    plt.plot(x, y)
    plt.title("line graph")
    plt.xlabel("x-label")
    plt.ylabel("Y-label")
    plt.show()

def plot_bar():
    x = [5, 2, 9, 4, 7]
    y = [10, 5, 8, 4, 2]

    plt.bar(x, y)
    plt.title("bar graph")
    plt.xlabel("x-label")
    plt.ylabel("Y-label")
    plt.show()

def plot_hist():
    y = [10, 5, 8, 4, 2, 5, 10, 10]

    plt.hist(y)
    plt.title("histogram graph")
    plt.xlabel("x-label")
    plt.ylabel("Y-label")
    plt.show()

def plot_scat():
    x = [5, 2, 9, 4, 7]
    y = [10, 5, 8, 4, 2]

    plt.scatter(x, y)
    plt.title("scatter graph")
    plt.xlabel("x-label")
    plt.ylabel("Y-label")
    plt.show()
    plt.plot(x, y)
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('plot')
    plot_line()
    plot_bar()
    plot_hist()
    plot_scat()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
