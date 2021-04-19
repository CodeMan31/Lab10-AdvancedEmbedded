
import matplotlib.pyplot as plt
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])  # sets points to plotted
plt.ylabel('y')  # Sets label for y axis
plt.xlabel('x')  # Sets label for x axis
plt.axis([0, 4, 0, 16])  # Sets ranges for x axis(args 1 and 2) and y axis(args 3 and 4)
plt.show()  # shows the graph
