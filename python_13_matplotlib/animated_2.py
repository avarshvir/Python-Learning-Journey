import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()
bars = ax.bar(range(10), np.random.randint(1, 10, size=10))

# Set up the axis limits
ax.set_ylim(0, 15)

# Update function for the bar chart
def update(frame):
    for bar in bars:
        bar.set_height(np.random.randint(1, 15))
    return bars

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=500, blit=True)

# Display the animation
plt.show()
