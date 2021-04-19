import numpy as np
import matplotlib.pyplot as plt


def math_fun(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)   # returns result of equation with argument t


t1 = np.arange(0.0, 5.0, 0.1)   # returns array of evenly spaced values with a given interval
t2 = np.arange(0.0, 5.0, 0.02)  # ^
plt.figure(1)   # the argument of this function changes the title in the context figure <argument>, only takes ints
plt.subplot(211)    # creates one of the plots to be shown
plt.plot(t1, math_fun(t1), 'r+', t2, math_fun(t2), 'k')  # below
# plt.plot(t1, np.cos(t1), 'r+', t2, math_fun(t2), 'k')
plt.grid()  # creates a grid for the plot

plt.subplot(212)    # creates one of the plots to be shown
plt.plot(t2, np.cos(2 * np.pi * t2), 'b--')  # below
# plt.plot(np.cos(2 * np.pi * t2))  # below
plt.grid()    # creates a grid for the plot
plt.show()  # shows plots

# first plot graphs t1, the math function with arg t1 as 'r+'*, t2, and math function with arg t2 as 'k'*
# r+ and k, change what the lines of the plot look like. The commented out lines of code are tests of
# other options look like. r is red and the + indicates the shape of points.#

# second plot graphs t2 and cos(2pi*t2), uses a blue dashed line indicating by b--. #
