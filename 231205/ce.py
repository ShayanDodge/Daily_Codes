import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 2 * np.pi, 400)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a plot with two curves and a legend
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.fill_between(x, y1, y2, where=y1 > y2, interpolate=True, alpha=0.2)

# Add text to the plot
plt.text(0.5 * np.pi, 0.5, 'Fill between curves', fontsize=12, ha='center')

# Set the x and y axis labels
plt.xlabel('x')
plt.ylabel('y')

# Set the title of the plot
plt.title('Text and fill between curves')

# Add a legend to the plot
plt.legend(['sin(x)', 'cos(x)', 'Area between curves'], loc='upper left')

# Show the plot
plt.show()