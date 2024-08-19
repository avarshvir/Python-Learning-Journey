import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Initialize data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a figure and axis
fig, ax = plt.subplots()
line, = ax.plot(x, y, 'r-')

# Set up the axis limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)

# Define the update function
def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))  # Update the y data of the line
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
