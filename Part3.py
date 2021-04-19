import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection="3d")  # creates the 3D model to be graphed on
z_line = np.linspace(0, 50, 1000)   # returns evenly space numbers over specified interval
# ^ first arg is the offset, the second arg is the y range, and the third arg seems to change the relationship
# between the x axis and the y axis#
x_line = np.exp(-0.1*z_line) * np.cos(z_line)  # creates line with given equation - 1
y_line = np.exp(-0.1*z_line) * np.sin(z_line)  # ^ - 2
# 1 [e ^ (-0.1 * z)] * cos(z)
# 2 [e ^ (-0.1 * z)] * sin(z)
ax.plot3D(x_line, y_line, z_line, 'red')    # plots 3 red lines based on the functions above
ax.set_xlabel("x")  # sets label of x axis to x
ax.set_ylabel("y")  # sets label of y axis to y
ax.set_zlabel("z")  # sets label of z axis to z
plt.show()  # shows graph
