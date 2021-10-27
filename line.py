# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from matplotlib import pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def plot_exp():
    x = [i for i in range(15)]
    y1 = [6.468, 9.551, 12.634, 15.718, 18.801, 21.885, 24.968, 28.052, 31.135, 34.218, 37.302, 40.385, 43.469, 46.552, 49.636]
    y2 = [6.515, 9.456, 12.682, 16.193, 19.990, 24.073, 28.440, 33.094, 38.032, 43.257, 48.766, 54.561, 60.642, 67.007, 73.658]


    plt.plot(x, y1, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12,
             label="linear fit exponent")
    plt.plot(x, y2, color='orange', marker='o', linewidth=2, markersize=12, label="2nd degree poly fit exponent")
    #plt.axis([0, 10, 0, 20]) # [xmin, xmax, ymin, ymax]
    plt.title("post FEC BER projection")
    plt.legend()
    plt.show()

def plot_ber():
    x = [i for i in range(16)]
    y1 = [3.405e-07, 2.810e-10, 2.319e-13, 1.914e-16, 1.579e-19, 1.303e-22, 1.076e-25, 8.877e-29, 7.325e-32, 6.045e-35,
          4.989e-38, 4.117e-41, 3.398e-44, 2.804e-47, 2.314e-50, 1.910e-50]
    y2 = [3.052e-07, 3.498e-10, 2.078e-13, 6.400e-17, 1.021e-20, 8.449e-25, 3.623e-29, 8.050e-34, 9.271e-39, 5.534e-44,
          1.712e-49, 2.745e-55, 2.282e-61, 9.828e-68, 2.194e-74, 2.539e-81]


    plt.plot(x, y1, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12,
             label="linear fit exponent")
    plt.plot(x, y2, color='orange', marker='o', linewidth=2, markersize=12, label="2nd degree poly fit exponent")
    plt.axis([0, 16, 1.0e-90, 1.0e-7]) # [xmin, xmax, ymin, ymax]
    plt.title("post FEC BER projection")
    plt.legend()
    plt.yscale('log')
    plt.show()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = [i for i in range(16)]

    #fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    #ax1.plot(x, e1, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12,
    #         label="linear fit exponent")
    #ax1.plot(x, e2, color='orange', marker='o', linewidth=2, markersize=12, label="2nd degree poly fit exponent")
    #ax1.set_title("post FEC BER projection")
    #ax1.legend()

    b1 = [3.405e-07, 2.810e-10, 2.319e-13, 1.914e-16, 1.579e-19, 1.303e-22, 1.076e-25, 8.877e-29, 7.325e-32, 6.045e-35,
          4.989e-38, 4.117e-41, 3.398e-44, 2.804e-47, 2.314e-50, 1.910e-53]
    b2 = [3.052e-07, 3.498e-10, 2.078e-13, 6.400e-17, 1.021e-20, 8.449e-25, 3.623e-29, 8.050e-34, 9.271e-39, 5.534e-44,
          1.712e-49, 2.745e-55, 2.282e-61, 9.828e-68, 2.194e-74, 2.539e-81]

    fig = plt.figure(figsize=(8,6))
    ax = plt.subplot(111)
    ax.plot(x, b1, color='green', marker='*', linewidth=2, markersize=8, label="linear fit exponent")
    ax.plot(x, b2, color='orange', marker='*', linewidth=2, markersize=8, label="2nd degree poly fit exponent")
    ax.set_title("post FEC BER projection")
    ax.set_yscale('log')
    ax.set_xlabel("prbs error bin t=")
    ax.set_ylabel("prbs ber in log format")
    xd = [0, 1, 2]
    yd = [3.052e-07, 3.498e-10, 2.078e-13]
    ax.scatter(xd, yd, s=200, c='r')
    for i in range(3):
        x = xd[i]
        y = yd[i]
        s = 'sample' + str(i)
        ax.text(x, y, s)
    ax.legend()
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
